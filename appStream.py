import socket
import json

# Conectar a NeuroSky MindWave
def conectar_neurosky():
    host = '127.0.0.1'
    port = 13854
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall('{"enableRawOutput": true, "format": "Json"}\n'.encode('utf-8'))
    print("Conectado a NeuroSky")
    return sock

# Conectar al servidor TCP (puerto 5000)
def conectar_servidor():
    server_host = '127.0.0.1'  # IP del servidor
    server_port = 5000  # Puerto del servidor
    try:
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.connect((server_host, server_port))
        print(f"Conectado al servidor en {server_host}:{server_port}")
        return server_sock
    except Exception as e:
        print(f"Error al conectar con el servidor TCP: {e}")
        return None

# Leer y filtrar datos, guardándolos en disco y enviándolos al servidor TCP
def leer_datos(sock, server_sock):
    try:
        with open("datos.json", "w") as archivo:  # Abre el archivo para escritura
            while True:
                data = sock.recv(1024)
                if data:
                    try:
                        json_data = json.loads(data.decode('utf-8'))

                        # Filtrar solo los datos que nos interesan
                        if all(k in json_data for k in ["eSense", "eegPower", "poorSignalLevel"]):
                            print(json_data)  # Mostrar en consola
                            
                            # Guardar en archivo
                            json.dump(json_data, archivo)
                            archivo.write("\n")  # Nueva línea para cada entrada
                            
                            # Enviar al servidor TCP si está conectado
                            if server_sock:
                                try:
                                    server_sock.sendall((json.dumps(json_data) + "\n").encode('utf-8'))
                                except Exception as e:
                                    print(f"Error al enviar datos al servidor: {e}")
                                    server_sock = None  # Evita seguir intentando enviar si el servidor se cae

                    except json.JSONDecodeError:
                        print("Error al decodificar JSON, saltando este paquete...")
    except KeyboardInterrupt:
        print("Cerrando conexión.")
        sock.close()
        if server_sock:
            server_sock.close()

# Ejecutar conexión y lectura de datos
sock = conectar_neurosky()
server_sock = conectar_servidor()
leer_datos(sock, server_sock)

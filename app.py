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

# Leer y filtrar datos, guardándolos en disco
def leer_datos(sock):
    try:
        with open("datos_neurosky.json", "w") as archivo:  # Abre el archivo para escritura
            while True:
                data = sock.recv(1024)
                if data:
                    try:
                        json_data = json.loads(data.decode('utf-8'))

                        # Filtrar solo los datos que nos interesan
                        if all(k in json_data for k in ["eSense", "eegPower", "poorSignalLevel"]):
                            print(json_data)  # Mostrar en consola
                            json.dump(json_data, archivo)  # Guardar en archivo JSON
                            archivo.write("\n")  # Nueva línea para cada entrada

                    except json.JSONDecodeError:
                        print("Error al decodificar JSON, saltando este paquete...")
    except KeyboardInterrupt:
        print("Cerrando conexión.")
        sock.close()

# Ejecutar conexión y lectura de datos
sock = conectar_neurosky()
leer_datos(sock)

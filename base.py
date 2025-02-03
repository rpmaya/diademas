import socket
import json

def conectar_neurosky():
    host = '127.0.0.1'
    port = 13854
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall('{"enableRawOutput": true, "format": "Json"}\n'.encode('utf-8'))
    print("Conectado a NeuroSky")
    return sock

def leer_datos(sock):
    try:
        while True:
            data = sock.recv(1024)
            if data:
                json_data = json.loads(data.decode('utf-8'))
                print(json_data)
    except KeyboardInterrupt:
        print("Cerrando conexión.")
        sock.close()

# Ejecutar conexión y lectura de datos
sock = conectar_neurosky()
leer_datos(sock)
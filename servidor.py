import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(1)
print("Esperando conexión...")

conn, addr = server.accept()
print(f"Conectado a {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Datos recibidos: {data.decode()}")
    
conn.close()

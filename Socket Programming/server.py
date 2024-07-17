import socket

def start_server():
    s = socket.socket()
    s.bind(('localhost', 9999))
    s.listen(1)
    print("Server started. Waiting for connections...")

    while True:
        c, addr = s.accept()
        print(f"Connected with {addr}")
        data = c.recv(1024).decode()
        print(f"Received data: {data}")
        data = data.upper()
        c.send(bytes(data, "utf-8"))
        c.close()

start_server()


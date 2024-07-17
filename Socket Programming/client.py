import socket

def start_client():
    s = socket.socket()
    s.connect(('localhost', 9999))
    s.send(bytes(input("Enter the message: "), "utf-8"))
    print(s.recv(1024).decode())
    s.close()

start_client()


import socket
import sys

socket = socket.socket()
socket.bind(('localhost', 62000))
socket.listen(1)

new_sock, new_addr = socket.accept()

new_sock.send("It's working".encode())


message_from_client = new_sock.recv(1024)

if message_from_client == "Hi server":
    new_sock.send("It's 200OK".encode())
else:
    new_sock.send("404 Error".encode())


new_sock.close()
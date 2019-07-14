import socket
import sys

socket = socket.socket()
socket.bind(('localhost', 62000))
socket.listen(1)

new_sock, new_addr = socket.accept()

message_from_client = new_sock.recv(1024)

if message_from_client.decode('UTF-8') == "Hi server":
    new_sock.send("It's 200OK".encode('UTF-8'))
else:
    new_sock.send("404 Error".encode('UTF-8'))


new_sock.close()

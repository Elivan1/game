import socket
import sys

socket = socket.socket()
socket.connect(('localhost', 62000))

data = socket.recv(1024)

print(data.decode())

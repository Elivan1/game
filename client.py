import socket
import sys

socket = socket.socket()
socket.connect(('localhost', 62000))

socket.send("Hi serve".encode())

data = socket.recv(1024)

print(data.decode('UTF-8'))

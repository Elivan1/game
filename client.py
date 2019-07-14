import socket
import sys

socket = socket.socket()
socket.connect(('localhost', 62000))
data = socket.recv(1024)

new_sock, new_addr = socket.accept()
new_sock.send("Hi server".encode())

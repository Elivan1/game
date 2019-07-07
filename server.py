import socket
import sys

socket = socket.socket()
socket.bind(('localhost', 62000))
socket.listen(1)

new_sock, new_addr = socket.accept()

new_sock.send('hello man'.encode())
new_sock.close()
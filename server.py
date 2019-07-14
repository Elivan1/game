import socket
import os
import sys

map = open('MAP_1.txt', 'r')

socket = socket.socket()
socket.bind(('localhost', 62000))
socket.listen(1)

new_sock, new_addr = socket.accept()

new_sock.send(map.read().encode())


new_sock.close()

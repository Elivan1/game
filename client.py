import socket
import sys
import os

clear = lambda: os.system('cls')

socket = socket.socket()
socket.connect(('localhost', 62000))

data = socket.recv(1024)

print(data.decode())

while True:
    command = input()
    if command.upper()[0] in ['W', 'A', 'S', 'D']:
        socket.send(command.upper()[0].encode())

        clear()

        data = socket.recv(1024)

        print(data.decode())

    elif command == 'exit()':
        socket.send(command.encode())
        break

import socket
import os
import sys

map = open('MAP_1.txt', 'r')

new_map = []

for line in map:
    for x in line:
        if x == '\n':
            continue
        new_map += x

pos = 209

for i in range(len(new_map)):
    if new_map[i] == 'A':
        pos = i

def convert_to_string(map):
    string = ''
    for i in range(len(map)):
        string += map[i]
        if (i + 1) % 20 == 0:
            string += '\n'

    return string


socket = socket.socket()
socket.bind(('localhost', 62000))
socket.listen(1)

new_sock, new_addr = socket.accept()

new_sock.send(convert_to_string(new_map).encode())

while True:
    data = new_sock.recv(1024)

    if data.decode() == 'exit()':
        new_sock.close()
        break

    elif data.decode() == 'W':
        if new_map[pos - 20] == ' ':
            [new_map[pos], new_map[pos - 20]] = [new_map[pos - 20], new_map[pos]]
            new_sock.send(convert_to_string(new_map).encode())
            pos -= 20
        else:
            new_sock.send(convert_to_string(new_map).encode())
            new_sock.send("You can't go there".encode())

    elif data.decode() == 'A':
        if new_map[pos - 1] == ' ':
            [new_map[pos], new_map[pos - 1]] = [new_map[pos - 1], new_map[pos]]
            new_sock.send(convert_to_string(new_map).encode())
            pos -= 1
        else:
            new_sock.send(convert_to_string(new_map).encode())
            new_sock.send("You can't go there".encode())

    elif data.decode() == 'S':
        if new_map[pos + 20] == ' ':
            [new_map[pos], new_map[pos + 20]] = [new_map[pos + 20], new_map[pos]]
            new_sock.send(convert_to_string(new_map).encode())
            pos += 20
        else:
            new_sock.send(convert_to_string(new_map).encode())
            new_sock.send("You can't go there".encode())

    elif data.decode() == 'D':
        if new_map[pos + 1] == ' ':
            [new_map[pos], new_map[pos + 1]] = [new_map[pos + 1], new_map[pos]]
            new_sock.send(convert_to_string(new_map).encode())
            pos += 1
        else:
            new_sock.send(convert_to_string(new_map).encode())
            new_sock.send("You can't go there".encode())



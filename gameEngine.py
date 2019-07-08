import os

map = open('MAP_1.txt', 'r')

map_new = []
pos = None

def printMap(map):
    temp_map = ''
    for j in map:
        temp_map += j

    clear = lambda: os.system('cls')
    clear()
    print(temp_map)


for line in map:
    for j in line[0: len(line)]:
        map_new.append(j)

for i in range(len(map_new)):
    if (map_new[i] == 'A'):
        pos = i


printMap(map_new)
while True:
    command = input()
    if command in ['w', 'W']:
        if map_new[pos - 21] == ' ':
            [map_new[pos - 21], map_new[pos]] = ['A', ' ']
            pos -= 21
    elif command in ['s', 'S']:
        if map_new[pos + 21] == ' ':
            [map_new[pos + 21], map_new[pos]] = ['A', ' ']
            pos += 21
    elif command in ['a', 'A']:
        if map_new[pos - 1] == ' ':
            [map_new[pos - 1], map_new[pos]] = ['A', ' ']
            pos -= 1
    elif command in ['d', 'D']:
        if map_new[pos + 1] == ' ':
            [map_new[pos + 1], map_new[pos]] = ['A', ' ']
            pos += 1
    printMap(map_new)
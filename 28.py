#!/usr/bin/python

from numpy import zeros, flipud

#max_x = 5
#max_y = 5
max_x = 1001
max_y = 1001


matriz = zeros((max_y, max_x))

x = max_x/2
y = max_y/2

n = 1
matriz[y][x] = n

n += 1
x += 1
matriz[y][x] = n

while x < max_x and y < max_y:

    # abajo
    while matriz[y][x-1] != 0:
        n += 1
        y += 1
        matriz[y][x] = n

    # izquierda
    while matriz[y-1][x] != 0:
        n += 1
        x -= 1
        matriz[y][x] = n

    # arriba
    while matriz[y][x+1] != 0:
        n += 1
        y -= 1
        matriz[y][x] = n

    # derecha
    while matriz[y+1][x] != 0:
        n += 1
        x += 1

        # llene la matriz
        if x == max_x:
            break

        matriz[y][x] = n

#print matriz
print sum(matriz.diagonal()) + sum(flipud(matriz).diagonal()) - 1

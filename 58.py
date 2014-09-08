#!/usr/bin/python

from numpy import zeros, flipud
from pyprimes import isprime


def formar_matriz(max_x, max_y):
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
            if x < 0:
                break

            matriz[y][x] = n

        # arriba
        while matriz[y][x+1] != 0:
            n += 1
            y -= 1

            if y < 0:
                break

            matriz[y][x] = n

        # derecha
        while matriz[y+1][x] != 0:
            n += 1
            x += 1

            # llene la matriz
            if x == max_x:
                break

            matriz[y][x] = n

    return matriz


tope = 7
while True:
    matriz = formar_matriz(tope, tope) # estetica

    a = list(matriz.diagonal())
    b = list(flipud(matriz).diagonal())

    r = 0
    for n in a + b:
        if isprime(int(n)):
            r += 1

    ratio = float(r)/len(a+b)

    print tope, ratio

    if ratio < 0.1:
        break

    tope += 2 #siempre impares

print matriz

#print sum(matriz.diagonal()) + sum(flipud(matriz).diagonal()) - 1

#!/usr/bin/python

def reducir(filas):
    if len(filas) == 1:
        print filas[0]
    else:

        for x in range(len(filas[-2])):
            v = filas[-2][x]
            i = filas[-1][x]
            d = filas[-1][x+1]

            if v + i > v + d:
                filas[-2][x] = v + i
            else:
                filas[-2][x] = v + d

        filas.pop(-1)
        reducir(filas)

filas = []
#for l in open("ejemplo.txt").readlines():
for l in open("18.txt").readlines():
    fila = []
    for n in l.strip().split(' '):
        fila.append(int(n))

    filas.append(fila)

reducir(filas)

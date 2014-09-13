#!/usr/bin/python

def esDecre(n):
    n = str(n)
    for x in range(len(n)-1):
        if int(n[x]) < int(n[x+1]):
            return 0
    return 1


def esIncre(n):
    n = str(n)
    for x in range(len(n)-1):
        if int(n[x]) > int(n[x+1]):
            return 0
    return 1


def tipoNumero(n):
    if esIncre(n): return 1
    elif esDecre(n): return -1
    else: return 0

numeros = {-1: 0, 0: 0, 1: 0}
n = 0 #n es a la vez el total de numeros que procesamos
tope = 10 ** 100

while n < tope:
    n += 1
    numeros[tipoNumero(n)] += 1

print numeros[0] + numeros[1]

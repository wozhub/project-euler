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

print 134468, tipoNumero(134468)
print 66420, tipoNumero(66420)
print 155349, tipoNumero(155349)

numeros = {-1: 0, 0: 0, 1: 0}
n = 0 #n es a la vez el total de numeros que procesamos
while True:
    n += 1
    numeros[tipoNumero(n)] += 1

    porc = float(numeros[0])/n

    if porc == 0.99:
        break

print numeros
print n

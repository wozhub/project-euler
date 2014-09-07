#!/usr/bin/python

from collections import deque

def esPrimo(n):
    n = abs(int(n))
    if n < 2:  return False
    if n % 2 == 0: return False
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True


def buscar_permutaciones(numero):
    d = deque(str(numero))

    permu = []
    for n in range(len(str(numero))):
        d.rotate()
        n = int(''.join(d))

        if len(str(n)) != len(str(numero)):
            continue

        if n not in permu:
            permu.append(n)

    return permu


def buscar_primos(tope):
    primos = [2, ]

    for n in range(3, tope, 2):
        if esPrimo(n):
            primos.append(n)

    return primos


print "Buscando primos"
#primos = buscar_primos(100)
primos = buscar_primos(1000000)

print "Buscando circulares"
circulares = []
for n in primos:
    circular = 1

    permutaciones = buscar_permutaciones(n)

    #print n, permutaciones

    for p in permutaciones:
        if p not in primos:
            circular = 0
            break

    if circular:
        circulares.append(n)

print circulares
print len(circulares)

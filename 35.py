#!/usr/bin/python

from collections import deque

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

    x = 1
    while True:
        no_primo = 0
        x += 2

        if x > tope:
            break

        for n in primos[1:]:
            #if n > x**0.5 + 10:  # optimizacion
            #    break

            if x % n == 0:
                no_primo = 1
                break

        if no_primo == 0:
            primos.append(x)

    return primos


print "Buscando primos"
primos = buscar_primos(1000)
print primos
#primos = buscar_primos(100)

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

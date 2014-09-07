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


def buscar_primos(tope):
    primos = [2, ]

    for n in range(3, tope, 2):
        if esPrimo(n):
            primos.append(n)

    return primos

tope = 100

while True:

    print "Buscando primos debajo de %d" % tope
    primos = buscar_primos(tope)

    print "Buscando truncables"

    t_ltr = []
    for n in primos:
        truncable = 1
        aux = str(n)

        if len(aux) < 2: continue

        for pos in range(len(aux)):
            if int(aux[pos:]) not in primos:
                truncable = 0
                break

        if truncable == 1:
            t_ltr.append(n)

    t_ltr_rtl = []
    for n in t_ltr:
        truncable = 1
        aux = str(n)

        if len(aux) < 2: continue

        for pos in range(1, len(aux)):
            if int(aux[:-pos]) not in primos:
                truncable = 0
                break

        if truncable == 1:
            t_ltr_rtl.append(n)

    if len(t_ltr_rtl) == 11:
        break
    else:
        print "No encontre suficientes (%d)..." % len(t_ltr_rtl)
        tope = tope * 10

print t_ltr_rtl
print sum(t_ltr_rtl)

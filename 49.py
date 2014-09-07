#!/usr/bin/python

from itertools import permutations


def esPrimo(n):
    n = abs(int(n))
    if n < 2:  return False
    if n % 2 == 0: return False
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True


def permutaciones(numero):
    p = []
    for a in permutations(str(numero)):
        n = int(''.join(a))
        if len(str(n)) < len(str(numero)):
            continue
        if esPrimo(n):
            if n not in p:
                p.append(int(''.join(a)))
    return sorted(p)


def buscar_primos(base, tope):
    primos = []
    for n in range(base, tope, 2):
        if esPrimo(n):
            primos.append(n)
    return primos


# 4 digitos solamente
primos = buscar_primos(999, 9999)

for p in primos:
    seq = 1
    per = permutaciones(p)

    if len(per) < 3:
        continue

    #if per[1] - per[0] == per[2] - per[1]:
    print p, per

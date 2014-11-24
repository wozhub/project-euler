#!/usr/bin/python

from numpy import zeros, flipud
from pyprimes import isprime


def esPandigital(n):
    n = str(n).replace('0', '')
    l = []
    for x in n:
        if x not in l:
            l.append(x)

    if len(l) == 9:
        return 1
    return 0


numero = 987654321
while True:
    if isprime(numero):
        if esPandigital(numero):
            print numero
            break
    numero -= 1

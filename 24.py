#!/usr/bin/python

from itertools import permutations


def permutaciones(cadena):
    p = []
    for a in permutations(cadena):
        p.append(''.join(a))
    return p

# print permutaciones('012')

print permutaciones('0123456789')[999999]

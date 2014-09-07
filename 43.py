#!/usr/bin/python

from itertools import permutations

perm = []
for p in permutations('0123456789'):
    if p[0] != '0':
        perm.append(''.join(p))

suma = 0
for n in perm:
    if int(n[1:4]) % 2 != 0:
        continue
    if int(n[2:5]) % 3 != 0:
        continue
    if int(n[3:6]) % 5 != 0:
        continue
    if int(n[4:7]) % 7 != 0:
        continue
    if int(n[5:8]) % 11 != 0:
        continue
    if int(n[6:9]) % 13 != 0:
        continue
    if int(n[7:10]) % 17 != 0:
        continue

    suma += int(n)

print suma

#!/usr/bin/python


def reversible(n):
    rev = int(str(n)[::-1])
    numero = str(n + rev)

    for x in numero:
        if int(x) % 2 == 0:
            return 0

    print n, rev, numero
    return 1


n = 0
#tope = 10**9
tope = 1000
reversibles = 0
while True:
    n += 1

    if n == tope:
        break

    if reversible(n):
        reversibles += 1

print reversibles

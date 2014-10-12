#!/usr/bin/python

from pyprimes import primes

p = primes()

while True:
    n = p.next()
    c = str(n)
    s = set(c)

    if len(c) > 10:
        break

    if len(s) >= len(c) - 1 :
        maximo = n

print maximo


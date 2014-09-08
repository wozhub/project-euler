#!/usr/bin/python

from pyprimes import factorise

n = 0
while True:
    n += 1

    a = set(factorise(n))
    if len(a) < 4: continue

    b = set(factorise(n+1))
    if len(b) < 4: continue

    c = set(factorise(n+2))
    if len(c) < 4: continue

    d = set(factorise(n+3))
    if len(d) < 4: continue

    if len(a & b & c & d) == 0:
        print n
        break

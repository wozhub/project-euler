#!/usr/bin/python

from math import factorial as f


def combinaciones(n, r):
    return (f(n))/(f(r)*f(n - r))


total = 0
for n in range(1, 101):
    for r in range(1, n):
        if combinaciones(n, r) > 1000000:
            total += 1

print total

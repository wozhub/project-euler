#!/usr/bin/python

def sumadigitos(n):
    suma=0
    for d in n:
        suma+=int(d)
    return suma

max=0
for a in range(1,100):
    for b in range(1,100):
        s=sumadigitos(str(a**b))
        if s > max:
            max=s

print max

#!/usr/bin/python

def triangulo(n): return (n*(n+1))/2
def hexagono(n): return (n*(3*n-1))/2
def pentagono(n): return n*(2*n-1)

t=[]
p=[]
h=[]
for n in range(1,100000):
    t.append(triangulo(n))
    p.append(pentagono(n))
    h.append(hexagono(n))

for elemento in t:
    if elemento in p:
        if elemento in h:
            print elemento

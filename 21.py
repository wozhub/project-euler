#!/usr/bin/python

def sumaDivisores(numero):
    a=0
    for n in range(1,numero):
        if numero%n==0:
            a+=n
    return a

suma=0
for n in range(1,10000):
    divisores=sumaDivisores(n)
    if divisores==n:
        continue
    if sumaDivisores(divisores)==n:
        print n,divisores
        suma+=n

print suma
print range(1,10)

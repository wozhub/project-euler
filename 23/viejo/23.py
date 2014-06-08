#!/usr/bin/python

def sumaDivisores(numero):
    a=0
    for n in range(1,numero):
        if numero%n==0: a+=n
    return a


enteros=[]
abundantes=[]
deficientes=[]
perfectos=[]

for entero in range(1,28123):
    if ( entero > 30 and entero%2==0) : continue
    enteros.append(entero)

for a1 in range(1,28123):
    if a1>sumaDivisores(a1): continue
    for a2 in range(1,a1+1):
        if a2>sumaDivisores(a1): continue

        a3=a1+a2
        if a3 in enteros:
            #print a1,a2,a3
            enteros.remove(a3)

    print len(enteros)

print enteros

suma=0
for a in enteros:
    suma+=a

print a

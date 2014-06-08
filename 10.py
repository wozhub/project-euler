#!/usr/bin/python

#from math import pow

lista=[2]
MAX=2000000

x=3
print "Armo la lista de numeros"
while x<MAX:

    primo=1
    for y in lista:
        if x%y==0:
            primo=0
            break

    if primo==1:
        lista.append(x)
    x+=2

"""for x in lista:
    if x*x > MAX:
        break

    potencia=2
    while 1:
        y=pow(x,potencia)
        if y > MAX:
            break
        if y in lista:
            lista.remove(y)
        potencia+=1"""

print "Hago la suma..."
suma=0
for x in lista:
    suma+=x

print suma

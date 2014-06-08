#!/usr/bin/python

from math import factorial

x=2
while True:
    x+=1
    f=factorial(x)

    suma=0
    for digito in str(x):
        suma+=factorial(int(digito))

    if suma==x:
        print suma

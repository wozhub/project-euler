#!/usr/bin/python

from math import pow

sumadecuadrados=0
cuadradodelasuma=0

for x in range(101):
    sumadecuadrados=sumadecuadrados+pow(x,2)

for x in range(101):
    cuadradodelasuma=cuadradodelasuma+x
cuadradodelasuma=pow(cuadradodelasuma,2)

print "%f" % (cuadradodelasuma-sumadecuadrados)

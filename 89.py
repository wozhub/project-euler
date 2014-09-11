#!/usr/bin/python

import serpente

with open('./p089_roman.txt') as archivo:
    numeros = [line.rstrip() for line in archivo]

suma = 0
for r in numeros:
    d = serpente.decode(r)
    correcto = serpente.encode(d)
    suma += len(r) - len(correcto)

print suma

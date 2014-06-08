#!/usr/bin/python

total=0
with open('names.txt', 'r') as archivo:
    linea=0
    for nombre in archivo:
        linea+=1
        nombre=nombre.rstrip()
        suma=0
        for letra in nombre:
            suma+=ord(letra)-64

        total+=(suma*linea)

print total

#!/usr/bin/python

from num2words import num2words


def escribir(numero):
    return num2words(numero).replace(' ', '').replace('-', '')


total = 0
for n in range(1, 1001):
    total += len(escribir(n))
print total




"""
total = 0
for n in range(1, 6):
    total += len(escribir(n))
print total

palabra = escribir(342)
print palabra, len(palabra)

palabra = escribir(115)
print palabra, len(palabra)
"""

#!/usr/bin/python

def factorial(numero):
    if numero == 1: return 1
    else:  return numero*factorial(numero-1)

suma=0
for n in str(factorial(100)):
    suma+=int(n)

print suma

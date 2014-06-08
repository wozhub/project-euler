#!/usr/bin/python

def divisores(numero):
    a=0
    for n in range(1,numero):
        if numero%n==0: a+=n
    return a

maximo=28123
abundantes=[]

print "Buscando Abundantes"
for numero in range(maximo):
    if numero < divisores(numero):
        abundantes.append(numero)

print "....................."
suma=0
for numero in range(maximo):

    for i in range(len(abundantes)):
        a1=abundantes[i]

        for j in range(len(abundantes)):
            a2=abundantes[j]

            if a1+a2==numero:
                break

            if a1+a2>numero:
                a2=abundantes[0]
                break

        if a1+a2>numero:
            suma+=numero
            break

print suma

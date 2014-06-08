#!/usr/bin/python

n=1
while True:
    suma=0
    for x in range(1,n+1):
        suma+=x

    divisores=0
    for x in range(1,suma+1):
        if suma%x==0: divisores+=1

    print suma,divisores

    if divisores>500:
        break

    n+=1

#!/usr/bin/python

lista=[]
for x in range(2,101):
    for y in range(2,101):
        n=x**y
        if n not in lista:
            lista.append(n)

print len(lista)

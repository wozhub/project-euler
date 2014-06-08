#!/usr/bin/python
x=0
seguir=1
divisores=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#divisores=[1,2,3,4,5,6,7,8,9,10]

while seguir:
    x=x+1
    seguir=0
    for n in divisores:
        if x%n!=0:
            seguir=1

print x

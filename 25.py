#!/usr/bin/python

x=1
y=0
z=0
t=0

while True:
    t+=1
    z=x+y
    x=y
    y=z

    if len(str(z)) >= 1000:
        print t
        break

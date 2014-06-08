#!/usr/bin/python

n=600851475143

for x in range(100000000):
    x=x+1
    if n%x==0:
        n=n/x
        print x,n

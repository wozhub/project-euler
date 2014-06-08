#!/usr/bin/python

suma=0
for n in range(1000000):
    if str(n) == str(n)[::-1]:
        if  str(bin(n))[2:] == str(bin(n))[:1:-1]:
            print n,str(bin(n))[2:]
            suma+=n

print "\n\n",suma

#!/usr/bin/python

n=1
suma=0
while n<250000:
    n+=1

    sumadepotencias=0
    for d in str(n):
        sumadepotencias+=int(d)**5

    if n == sumadepotencias:
        suma+=n
        print n

print "!",suma

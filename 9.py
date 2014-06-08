#!/usr/bin/python

for a in range(1,998):
    for b in range (a,999):
        c=1000-a-b
        if a*a+b*b==c*c:
            print a,b,c
            print a*b*c

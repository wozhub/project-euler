#!/usr/bin/python

def esPrimo(n):
    n = abs(int(n))
    if n < 2: return False
    if n == 2: return True
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
        return True

maxN=0

for a in range(-999,999):
    for b in range(-999,999):
        if not esPrimo(b):
            continue

        n=0

        while True:
            x=n^2+a*n+b

            if esPrimo(x):
                n+=1
            else:
                if n>maxN:
                    maxN=n
                    maxA=a
                    maxB=b
                break

print maxN,maxA*maxB

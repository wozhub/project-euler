#!/usr/bin/python

n = 0
while True:
    n += 1

    a = set(str(n))
    b = set(str(2*n))
    c = set(str(3*n))
    d = set(str(4*n))
    e = set(str(5*n))
    a = set(str(6*n))

    if a & b & c & d == a:
        print n
        break

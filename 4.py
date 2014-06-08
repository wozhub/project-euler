#!/usr/bin/python

# sort -n

for x in range(1000):
    for y in range(1000):
        z=x*y
        if str(z) == str(z)[::-1]:
            print "%d = %d * %d" % (z,x,y)

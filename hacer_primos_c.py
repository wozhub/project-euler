#!/usr/bin/python

from pyprimes import nprimes

primos = list(nprimes(1000000))

print "int primos[] = {"

for p in primos:
    print "%d, " % p,

print "};\n"

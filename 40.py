#!/usr/bin/python

i=""

for n in range(1,1000001):
#for n in range(1,20):
    i+=str(n)

mult=1
for n in i[0],i[9],i[99],i[999],i[9999],i[99999],i[999999]:
    mult=mult*int(n)

print mult

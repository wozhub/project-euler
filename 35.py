#!/usr/bin/python

naturales=[]
primos=[2,3,5,7,11,13,17,19,23,29,31,37]
#tope=104800
tope=1000000

print "Cargando lista de naturales"
x=1
while x<tope-2:
    x=x+2 #los pares ni los cargo
    #me fijo que no sea multiplo de los primeros primos, para optimizar
    #if x%2==0: continue
    if x%3==0: continue
    if x%5==0: continue
    if x%7==0: continue
    if x%11==0: continue
    if x%13==0: continue
    if x%17==0: continue
    if x%19==0: continue
    if x%23==0: continue
    if x%29==0: continue
    if x%31==0: continue
    if x%37==0: continue
    naturales.append(x)
naturales.reverse()

print "%d naturales impares donde buscar primos" % len(naturales)

while naturales:
    n=naturales.pop()
    if n not in primos:
        primos.append(n)

        x=1
        m=n
        while m <= tope:
            if m in naturales:
                naturales.remove(m)
            x=x+1
            m=n*x

print "Encontre %d primos" % len(primos)
print "1: %d" % primos[0]
print "10 001: %d" % primos[10000]
print "10 000: %d" % primos[9999]

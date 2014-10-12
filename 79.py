#!/usr/bin/python

# los numeros no se repiten...

numeros = {

}

lineas = []
for l in [l.strip() for l in open("./keylog.txt")]:
    lineas.append(l)

for l in lineas:
    for i in range(len(l)):
        if i > 0:
            pass
        if i < 2:
            pass

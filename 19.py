#!/usr/bin/python

from datetime import date, timedelta

fecha = date(1901, 1, 1)
dia = timedelta(1)

domingos = 0
while True:
    f = fecha.timetuple()

    # si es domingo y primer dia del mes
    if f[6] == 6 and f[2] == 1:
        domingos += 1
        print fecha,

    fecha += dia

    if fecha.timetuple()[0] == 2001:
        break

print "\n", domingos

#!/usr/bin/python

# primero ordene el archivo de mayor a menor
# cat p099_base_exp.txt | sort -n -r > 1; mv 1 p099_base_exp.txt

from math import log

linea_n = 0
with open('./p099_base_exp.txt') as archivo:
    max_log = 0
    for linea in archivo.readlines():
        linea_n += 1
        base, exponente = linea.rstrip().split(',')
        base = int(base)
        exponente = int(exponente)
        l = exponente * log(base)

        if l > max_log:
            max_log = l
            max_linea = linea_n

print max_linea

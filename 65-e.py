#!/usr/bin/python

#http://projecteuler.net/problem=65
"""      1          2         5         12        29
    1 + --- ;  1 + --- ; 1 + --- ; 1 + --- ; 1 + ---
         2          5         12        29        70
"""

def numerador(profundidad):
    return denominador(profundidad-1)+denominador(profundidad)

def denominador(profundidad):
    if profundidad==0: return 1
    elif profundidad<0: return 0
    else: return 2*denominador(profundidad-1)+denominador(profundidad-2)

for n in range(0,10):
    print "%d / %d" % ( numerador(n),denominador(n) )


#!/usr/bin/python

#http://projecteuler.net/problem=65

# raiz 2
"""      1          2         5         12        29
    1 + --- ;  1 + --- ; 1 + --- ; 1 + --- ; 1 + ---
         2          5         12        29        70
"""

# e
"""          8    11    19     87   106   192   1264
    2 ; 3 ; --- ; --- ; --- ; --- ; --- ; --- ; ---
             3     4     7     32    39    71   465
"""

def numerador2(profundidad):
    return denominador2(profundidad-1)+denominador2(profundidad)

def denominador2(profundidad):
    # Casos base para la recursividad
    if profundidad == 0:
        return 1
    elif profundidad < 0:
        return 0
    # El denominador es dos veces el anterior mas el anterior del anterior
    else:
        return 2*denominador2(profundidad-1)+denominador2(profundidad-2)

for n in range(0, 10):
    print "%d / %d" % (numerador2(n), denominador2(n))

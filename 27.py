#!/usr/bin/python


def esPrimo(n):
    n = abs(int(n))
    if n < 2:  return False
    if n % 2 == 0: return False
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True


def contarGenerados(a, b):
    n = 0
    primos = 0
    while True:
        generado = n**2 + a*n + b
        if esPrimo(generado):
            primos += 1
            n += 1
        else:
            break
    return primos


"""print contarGenerados(1, 41)
print contarGenerados(-79, 1601)"""

maximo = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):

        generados = contarGenerados(a, b)
        if generados > maximo:
            maximo = generados
            max_a = a
            max_b = b

print max_a*max_b

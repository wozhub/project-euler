#!/usr/bin/python


def divisores(numero):
    divisores = []
    for divisor in range(1, numero/2):
        if numero % divisor == 0:
            divisores.append(divisor)
    return divisores


def tipo_de_numero(numero):
    d = sum(divisores(numero))
    if d < numero:
        return -1
    elif d == numero:
        return 0
    return 1


def sumaAbundantes(numero):
    for a in abundantes:

        if a > numero:
            return 0

        for b in abundantes[1::]:
            if a == b:
                continue
            if a + b > numero:
                break
            if a + b == numero:
#                print "%d + %d = %d" % (a, b, numero)
                return 1
    return 0


"""print 28, tipo_de_numero(28)
print 12, tipo_de_numero(12)"""

print "Buscando abundantes..."
abundantes = []
for n in range(1, 28123):
    if tipo_de_numero(n) == 1:
        abundantes.append(n)

print "Buscando enteros que no sean abundantes sumados"
suma = 0
for n in range(1, 28123):
    if sumaAbundantes(n):
        continue
    else:
        suma += n
        print suma

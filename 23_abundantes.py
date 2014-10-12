#!/usr/bin/python


def divisores(numero):
    divisores = []
    for divisor in range(1, numero/2 + 1):
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


total = 0
print "int abundantes[] = {"
for n in range(1, 28123):
    if tipo_de_numero(n) == 1:
        print "%d, " % n,
        total += 1
print "}; /* %d */\n" % total

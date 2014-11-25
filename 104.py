#!/usr/bin/python


# http://technobeans.wordpress.com/2012/04/16/5-ways-of-fibonacci-in-python/
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]


@Memoize
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def esPandigital(n):
    l = []
    for x in n:
        if x not in l:
            l.append(x)

    if len(l) == 9:
        return 1
    return 0


indice = 0
while True:
    indice += 1
    comienza, termina = 0, 0

    f = fib(indice)
    n = str(f)

    if '0' in n[:9]:
        continue

    if esPandigital(n[:9]):
        comienza=1
        print indice, n

    if '0' in n[-9:]:
        continue

    if esPandigital(n[-9:]):
        termina=1
        print indice, n


    if comienza and termina:
        break

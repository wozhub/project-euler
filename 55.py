#!/usr/bin/python

# http://stackoverflow.com/questions/19365008/python-function-to-check-for-palindrome
def es_palindromo(num):
    num = str(num)
    return num == num[::-1]

l = []
for n in range(1, 10000):

    i = 0
    lychrel = n
    while True:

        if i == 50:
            break

        m = int(str(n)[::-1])
        n = n + m

        if es_palindromo(n):
            lychrel = 0
            break
        else:
            i += 1

    if lychrel != 0:
        l.append(lychrel)

print len(l)

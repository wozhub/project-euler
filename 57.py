#!/usr/bin/python

#http://projecteuler.net/problem=65

# raiz 2
"""      1          2         5         12        29
    1 + --- ;  1 + --- ; 1 + --- ; 1 + --- ; 1 + ---
         2          5         12        29        70
"""

num = [1, 3]
den = [1, 2]
total = 0
for p in range(2, 1000):
    d = 2*den[p-1]+den[p-2]
    den.append(d)
    n = den[p-1]+den[p]
    num.append(n)

    if len(str(n)) > len(str(d)):
        total += 1

print total

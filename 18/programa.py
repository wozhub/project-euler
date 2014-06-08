#!/usr/bin/python

filas=[]
for l in open("triangle.txt").readlines():
    fila=[]
    for elemento in l.strip().split(' '):
        fila.append(int(elemento))
    filas.append(fila)

suma=0
x=2
y=4

while y < len(filas)-1:
    print filas[y][x]
    suma+=filas[y][x]

    y+=1
    mX=len(filas[y]) #maximo x
    if x==mX: #no puedo avanzar a la derecha
        if filas[y][x] > filas[y][x-1]: x-=1
    elif x==0: #no puedo avanzar a la izquierda
        if filas[y][x] > filas[y][x+1]: x+=1
    else:
        if filas[y][x] > filas[y][x-1]:
            if filas[y][x] > filas[y][x+1]: pass
            else: x+=1
        else:
            if filas[y][x-1] > filas[y][x+1]: x-=1
            else: x+=1

print "\n\n",suma

#!/usr/bin/python

from pokereval import PokerEval

p = PokerEval()

contador = 0
with open('./p054_poker.txt') as archivo:
    for juego in archivo:
        cartas = juego.rstrip().lower().split(' ')

        mano_a, mano_b = cartas[:5], cartas[5:]

        if p.evaln(mano_a) > p.evaln(mano_b):
            contador += 1

print contador

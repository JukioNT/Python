#!/usr/bin/env python
# -*- coding> utf-8 -*-

nome = input("Digite seu nome \n>")
nome = nome.title()
nome = nome.replace(" Da ", " da ")
nome = nome.replace(" De ", " de ")

frase = "Oi {nome}. Tudo nem?"
print(frase)

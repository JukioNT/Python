#!/usr/bin/env python
# -*- coding> utf-8 -*-

nome = input("Digite seu nome \n>")
nome = nome.title()
nome = nome.replace(" Da ", " da ")
nome = nome.replace(" De ", " de ")

frase = "Oi {nome}. Tudo bem?"
print(frase.format(nome=nome))
print("Comigo tudo bem!")
print("Vamos brincar?")
print("Vamos correr?")
print(";-D")
#!/usr/bin/env python
# -*- coding> utf-8 -*-

print(".:: No Bar ::. \n")

resposta = "sim"

while resposta in "sim":
    resposta = input("Mais uma cerveja? [sim/não]: ")
    resposta = resposta.lower()
    if resposta in "sim":
        print("bebendo")

print("casa")


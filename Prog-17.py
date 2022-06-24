#!/usr/bin/env python
# -*- coding> utf-8 -*-

print(".:: No Bar ::. \n")

resposta = "sim"

while True:
    resposta = input("Mais uma cerveja? [sim/não]: ")
    resposta = resposta.lower()
    if resposta in ["sim", "mais", "mais uma", "beleza", "ok"]:
        print("bebendo")
    else:
        break

print("casa")


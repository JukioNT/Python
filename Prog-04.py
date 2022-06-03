#!/usr/bin/env python
# -*- coding> utf-8 -*-

print(":: Conversor de m/s para km/h::".center(80, "."))

entrada = float(input("Digite a velocidade(m/s)\n>"))

v_ms = float(entrada)
v_kmh = v_ms * 3.6

print("{0:.3f}m/s = {1:.3f}Km/h".format(v_ms, v_kmh))

#!/usr/bin/env python
# -*- coding> utf-8 -*-

print(".:: for vs while ::. \n")

print("For in")
turma = [4, 5, 1, 2, 9, 3]
for nota_aluno in turma:
    print(nota_aluno**2 - 5)
print("Ufa!!!")

print("\nWhile")
turma = [4, 5, 1, 2, 9, 3]
i = 0
while i < len(turma):
    print(turma[i]**2 - 5)
    i += 1
print("Ufa!!!")

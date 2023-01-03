import random


matriz = []
linha = []
coluna = []
lados = 15
contador = 0

matriz = [[random.choice(["0","1"]) for x in range(lados)] for y in range(lados)]
matriz[0][2] = "\u2609"

for linha in matriz:
  print(' '.join(linha))

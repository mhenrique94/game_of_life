import random
import os
import time

os.system("clear")
print("john conway's game of life by m. silva \n")
loop = int(input("Insira a quantidade de interações celulares que gostaria de ver (recomendo acima de 100): "))

col_line_range = 25

initial_matrix = [[random.choice(["\u2609"," "]) for x in range(col_line_range)] for y in range(col_line_range)]
next_matrix = [[ " " for x in range(col_line_range)] for y in range(col_line_range)]


def neighbours(x, y):
  neighbourhood = 0;
  for dx in range (-1, 2):
    for dy in range (-1, 2):
      neighbourX = x + dx;
      neighbourY = y + dy;
      if (dx != 0 or dy != 0) and neighbourX >= 0 and neighbourX < col_line_range and neighbourY >= 0 and neighbourY < col_line_range and initial_matrix[neighbourX][neighbourY] == "\u2609":
        neighbourhood+=1

  return neighbourhood;

def create_next_matrix(initial_matrix):
    for idx, row in enumerate(initial_matrix):
        for idy, col in enumerate(row):
          live_neighbours = neighbours(idx, idy)
          if live_neighbours < 2 or live_neighbours > 3:
              next_matrix[idx][idy] = " "
          elif live_neighbours == 3 and initial_matrix[idx][idy] == " ":
              next_matrix[idx][idy] = "\u2609"
          else:
              next_matrix[idx][idy] = initial_matrix[idx][idy]


cont = 0
while cont < loop:
  os.system("clear")

  print("john conway's game of life por m. silva \n")
  print("Segure CTRL + C para parar")

  create_next_matrix(initial_matrix)

  for line in next_matrix:
    print(' '.join(line))

  cont+= 1

  initial_matrix = next_matrix

  time.sleep(1 / 5.0)

if cont == loop:
  os.system("clear")
  print("john conway's game of life por m. silva")

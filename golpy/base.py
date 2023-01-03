import random

col_line_range = 25

initial_matrix = [[random.choice(["\u2609","0"]) for x in range(col_line_range)] for y in range(col_line_range)]
next_matrix = [[ " " for x in range(col_line_range)] for y in range(col_line_range)]


def neighbours(x, y):
  neighborhood = 0;
  for dx in range (-1, 2):
    for dy in range (-1, 2):
      neighbourX = x + dx;
      neighbourY = y + dy;
      if (dx != 0 or dy != 0) and neighbourX >= 0 and neighbourX < col_line_range and neighbourY >= 0 and neighbourY < col_line_range and initial_matrix[neighbourX][neighbourY] == "\u2609":
        neighborhood+=1

  return neighborhood;

def create_next_matrix(initial_matrix):
    for idx, row in enumerate(initial_matrix):
        for idy, col in enumerate(row):
          live_neighbours = neighbours(idx, idy)
          print(live_neighbours, end="")
          if live_neighbours < 2 or live_neighbours > 3:
              next_matrix[idx][idy] = "0"
          elif live_neighbours == 3 and initial_matrix[idx][idy] == "0":
              next_matrix[idx][idy] = "\u2609"
          else:
              next_matrix[idx][idy] = initial_matrix[idx][idy]

create_next_matrix(initial_matrix)
# cont = 0
print("\n")
for line in initial_matrix:
#   cont+= 1
  print(' '.join(line))

# for line in next_matrix:
#   print(' '.join(line))
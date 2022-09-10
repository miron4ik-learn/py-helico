from random import randint as rand

def randbool(r, mxr):
  temp = rand(0, mxr)
  return temp <= r

def randcell(width, height):
  temp_width = rand(0, width - 1)
  temp_height = rand(0, height - 1)
  return temp_height, temp_width

def randneighbour(x, y):
  # 0 – наверх, 1 – направо, 2 – вниз, 3 – налево
  moves = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
  temp = rand(0, 3)
  dx, dy = moves[temp][0], moves[temp][1]
  return x + dx, y + dy
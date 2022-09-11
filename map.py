from utils import randbool, randcell, randneighbour

# 0 – поле
# 1 – дерево
# 2 – река
# 3 – госпиталь
# 4 – апгрейд-шоп
# 5 – огонь

CELL_TYPES = '🟩🌲🌊🏥🏦🔥'

class Map:
  def __init__(self, width, height, helico):
    self.width = width
    self.height = height
    
    self.helico = helico
    
    self.cells = [ [ 0 for i in range(width) ] for j in range(height) ]
    
  def generate_river(self, len):
    rc = randcell(self.width, self.height)
    rx, ry = rc[0], rc[1]
    self.cells[rx][ry] = 2
    
    while len > 0:
      nc = randneighbour(rx, ry)
      nx, ny = nc[0], nc[1]
      
      if self.check_bounds(nx, ny):        
        self.cells[nx][ny] = 2
        rx, ry = nx, ny
        len -= 1
    
  def generate_forest(self, r, mxr):
    for ri in range(self.height):
      for ci in range(self.width):
        if randbool(r, mxr):
          self.cells[ri][ci] = 1
          
  def generate_tree(self):
    rc = randcell(self.width, self.height)
    rx, ry = rc[0], rc[1]
    
    if self.cells[rx][ry] == 0:
      self.cells[rx][ry] = 1
      
  def add_fire(self):
    rc = randcell(self.width, self.height)
    rx, ry = rc[0], rc[1]
    
    if self.cells[rx][ry] == 1:
      self.cells[rx][ry] = 5
      
  def update_fires(self):
    for ri in range(self.height):
      for ci in range(self.width):
        if self.cells[ri][ci] == 5:
          self.cells[ri][ci] = 0
          
    for i in range(5):
      self.add_fire()
    
  def check_bounds(self, x, y):
    return not (x < 0 or y < 0 or x >= self.height or y >= self.width)
    
  def print_map(self):
    print('⬛️' * (self.width + 2))
    
    for ri in range(self.height):
      print('⬛️', end='')
      
      for ci in range(self.width):
        cell = self.cells[ri][ci]
        
        if(self.helico.x == ri and self.helico.y == ci):
          print('🚁', end='')
        
        elif cell >= 0 and cell < len(CELL_TYPES):
          print(CELL_TYPES[cell], end='')
        else:
          print(CELL_TYPES[0], end='')
          
      print('⬛️')
    print('⬛️' * (self.width + 2))
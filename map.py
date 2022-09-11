from utils import randbool, randcell, randneighbour

# 0 – поле
# 1 – дерево
# 2 – река
# 3 – госпиталь
# 4 – апгрейд-шоп
# 5 – огонь

CELL_TYPES = '🟩🌲🌊🏥🏦🔥'

TREE_BONUS = 100
UPGRADE_COST = 500
LIFE_COST = 1000

class Map:
  def __init__(self, width, height, helico, clouds):
    self.width = width
    self.height = height

    self.helico = helico
    self.clouds = clouds
    
    self.cells = [ [ 0 for i in range(width) ] for j in range(height) ]
    
    self.generate_map()
    
  def generate_map(self):
    self.generate_forest(3, 10)
    self.generate_river(10)
    self.generate_river(10)
    self.generate_river(10)
    self.generate_upgrade_shop()
    self.generate_hospital()
    
  def generate_river(self, len):
    rx, ry = randcell(self.width, self.height)
    self.cells[rx][ry] = 2
    
    while len > 0:
      nx, ny = randneighbour(rx, ry)
      
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
    rx, ry = randcell(self.width, self.height)
    
    if self.cells[rx][ry] == 0:
      self.cells[rx][ry] = 1
      
  def add_fire(self):
    rx, ry = randcell(self.width, self.height)
    
    if self.cells[rx][ry] == 1:
      self.cells[rx][ry] = 5
      
  def update_fires(self):
    for ri in range(self.height):
      for ci in range(self.width):
        if self.cells[ri][ci] == 5:
          self.cells[ri][ci] = 0
          
    for i in range(10):
      self.add_fire()
      
  def generate_upgrade_shop(self):
    rx, ry = randcell(self.width, self.height)
    self.cells[rx][ry] = 4
    
  def generate_hospital(self):
    rx, ry = randcell(self.width, self.height)
    
    if self.cells[rx][ry] != 4:
      self.cells[rx][ry] = 3
    else:
      self.generate_hospital()
      
  def process_helico(self):
    hx = self.helico.x
    hy = self.helico.y
    cell = self.cells[hx][hy]
    
    if cell == 2:
      self.helico.tank = self.helico.max_tank
      
    elif cell == 5:
      if self.helico.tank > 0:
        self.helico.tank -= 1
        self.helico.score += TREE_BONUS
        self.cells[hx][hy] = 1
        
    elif cell == 4:
      if self.helico.score >= UPGRADE_COST:
        self.helico.max_tank += 1
        self.helico.score -= UPGRADE_COST
        
    elif cell == 3:
      if self.helico.score >= LIFE_COST:
        self.helico.lives += 50
        self.helico.score -= LIFE_COST
      
  def process_clouds(self):
    hx = self.helico.x
    hy = self.helico.y
    cloud = self.clouds.cells[hx][hy]
    
    if cloud == 2:
      self.helico.lives -= 1
      
      if self.helico.lives <= 0:
        self.helico.gameover()
    
  def check_bounds(self, x, y):
    return not (x < 0 or y < 0 or x >= self.height or y >= self.width)
    
  def print_map(self):
    print('⬛️' * (self.width + 2))
    
    for ri in range(self.height):
      print('⬛️', end='')
      
      for ci in range(self.width):
        cell = self.cells[ri][ci]
        
        if self.clouds.cells[ri][ci] == 1:
          print('⛅️', end='')
        elif self.clouds.cells[ri][ci] == 2:
          print('☔️', end='')
        
        elif(self.helico.x == ri and self.helico.y == ci):
          print('🚁', end='')
        
        elif cell >= 0 and cell < len(CELL_TYPES):
          print(CELL_TYPES[cell], end='')
        else:
          print(CELL_TYPES[0], end='')
          
      print('⬛️')
    print('⬛️' * (self.width + 2))
from utils import randbool

# 0 – ничего
# 1 – облако
# 2 – туча

class Clouds:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
    self.cells = [ [ 0 for i in range(width) ] for j in range(height) ]
    
  def update_clouds(self, r=2, mxr=10, g=3, mxg=10):
    for i in range(self.height):
      for j in range(self.width):
        if randbool(r, mxr):
          self.cells[i][j] = 1
          if randbool(g, mxg):
            self.cells[i][j] = 2
        else:
          self.cells[i][j] = 0
          
  def export_data(self):
    return {
      'cells': self.cells,
    }
    
  def import_data(self, data):
    self.cells = data['cells'] or [ [ 0 for i in range(self.width) ] for j in range(self.height) ]
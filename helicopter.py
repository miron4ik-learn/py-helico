from pynput import keyboard
from utils import randcell

class Helicopter:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
    rc = randcell(width, height)
    rx, ry = rc[0], rc[1]
    
    self.x = rx
    self.y = ry
    
    self.MOVES = { 'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1) }
    
    listener = keyboard.Listener(on_release=self.on_release)
    listener.start()
    
    self.tank = 0
    self.max_tank = 1
    
  def move(self, dx, dy):
    nx = dx + self.x
    ny = dy + self.y
    
    if nx >= 0 and ny >= 0 and nx < self.height and ny < self.width:
      self.x = nx
      self.y = ny
    
  def on_release(self, key):
    char = key.char.lower()
    if char in self.MOVES.keys():
      dx = self.MOVES[char][0]
      dy = self.MOVES[char][1]
      self.move(dx, dy)
      
  def print_menu(self):
    print('💦 ', self.tank, '/', self.max_tank, sep='')
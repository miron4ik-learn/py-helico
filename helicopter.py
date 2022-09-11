from pynput import keyboard
from utils import randcell

MOVES = { 'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1) }

class Helicopter:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
    rx, ry = randcell(width, height)
    self.x = rx
    self.y = ry
    
    self.tank = 0
    self.max_tank = 1
    
    self.score = 0
    
    listener = keyboard.Listener(on_release=self.on_release)
    listener.start()
    
  def move(self, dx, dy):
    nx = dx + self.x
    ny = dy + self.y
    
    if nx >= 0 and ny >= 0 and nx < self.height and ny < self.width:
      self.x = nx
      self.y = ny
    
  def on_release(self, key):
    char = key.char.lower()
    if char in MOVES.keys():
      dx, dy = MOVES[char]
      self.move(dx, dy)
      
  def print_menu(self):
    print('💦 ', self.tank, '/', self.max_tank, sep='', end = ' | ')
    print('🏆 ', self.score, sep='')
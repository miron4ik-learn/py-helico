import os

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
    self.lives = 100
    
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
      
  def gameover(self):
    os.system('cls')
    
    print('X' * 50)
    print('X', ' ' * 48, sep='')
    print('X', ' ' * 5, 'GAME OVER. YOUR SCORE IS ', self.score, sep='')
    print('X', ' ' * 48, sep='')
    print('X' * 50)
    
    exit(0)
      
  def print_menu(self):
    print('๐ฆ ', self.tank, '/', self.max_tank, sep='', end = ' | ')
    print('๐ ', self.score, sep='', end=' | ')
    print('๐งก ', self.lives, sep='')
    
  def export_data(self):
    return {
      'x': self.x,
      'y': self.y,
      'tank': self.tank,
      'max_tank': self.max_tank,
      'score': self.score,
      'lives': self.lives,
    }
    
  def import_data(self, data):
    self.x = data['x'] or 0
    self.y = data['y'] or 0
    self.tank = data['tank'] or 0
    self.max_tank = data['max_tank'] or 1
    self.score = data['score'] or 0
    self.lives = data['lives'] or 100
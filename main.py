import os
import time
import json

from pynput import keyboard

from map import Map
from clouds import Clouds
from helicopter import Helicopter as Helico

MAP_W, MAP_H = 20, 10

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATE = 100

helico = Helico(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
map = Map(MAP_W, MAP_H, helico, clouds)

tick = 1
  
def save():
  data = {
    'helicopter': helico.export_data(),
    'clouds': clouds.export_data(),
    'map': map.export_data(),
    'tick': tick,
  }
  
  with open('level.json', 'w') as lvl:
    json.dump(data, lvl)
  
def recovery():
  with open('level.json', 'r') as lvl:
    data = json.load(lvl)
    
    global tick
    tick = data['tick'] or 1
    
    helico.import_data(data['helicopter'])
    clouds.import_data(data['clouds'])
    map.import_data(data['map'])

# f – сохранение, g – восстановление
KEYS = { 'f': save, 'g': recovery }

def on_release(key):
  char = key.char.lower()
  if char in KEYS.keys():
    KEYS[char]()

listener = keyboard.Listener(on_release=on_release)
listener.start()

while True:
  os.system('cls')
  print('TICK', tick)
  
  helico.print_menu()
  map.print_map()
  
  map.process_helico()
  map.process_clouds()
  
  tick += 1
  time.sleep(TICK_SLEEP)
  
  if tick % TREE_UPDATE == 0:
    map.generate_tree()
    
  if tick % FIRE_UPDATE == 0:
    map.update_fires()
    
  if tick % CLOUDS_UPDATE == 0:
    clouds.update_clouds()
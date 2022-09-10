import os
import time
from map import Map

TICK_SLEEP = 0.05
TREE_UPDATE = 50

map = Map(20, 10)
map.generate_forest(3, 10)
map.generate_river(10)
map.generate_river(10)
map.generate_river(10)
map.print_map()

tick = 1
while True:
  os.system('cls')
  
  print('TICK', tick)
  map.print_map()
  
  tick += 1
  time.sleep(TICK_SLEEP)
  
  if tick % TREE_UPDATE == 0:
    map.generate_tree()
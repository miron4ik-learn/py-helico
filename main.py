import os
import time
from map import Map

TICK_SLEEP = 0.05

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
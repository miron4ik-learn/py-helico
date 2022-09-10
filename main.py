from map import Map

tmp = Map(10, 10)

tmp.cells[1][1] = 1
tmp.cells[2][2] = 2
tmp.cells[3][3] = 3
tmp.cells[4][4] = 4
tmp.cells[5][5] = -1

print(tmp.check_bounds(1, 9))
print(tmp.check_bounds(1, 10))

tmp.print_map()
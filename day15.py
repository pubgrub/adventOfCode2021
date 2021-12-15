# AdventOfCode 2021
# Day 15

#get input data

lines = []
with open( "15.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

gridSizeY = len(lines)
gridSizeX = len( lines[0])
grid = []
for l in lines:
    x = list( l)
    grid.append( x)

print( grid)
print( grid[0][0])
print( gridSizeX, gridSizeY)


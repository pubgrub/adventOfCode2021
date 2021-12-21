# AdventOfCode 2021
# Day 20

#get input data

lines = []
with open( "20.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

algorithm = {}
pixel = {}

for c in range( len( lines[0])):
  if lines[0][c] == '#':
    algorithm[ c] = 1

width = len(lines[2])


line = 0
for l in lines[ 2:]:
  for c in range( len( l)):
    if l[c] == '#':
      pixel[ ( line, c)] = 1
  line += 1

height = line

def process( pixel):
  newPixel = {}
  for l in range( -10, height + 10):
    for c in range( -10, width + 10):
      v = 0
      for yGrid in range( l - 1, l + 2):
        for xGrid in range( c - 1, c + 2):
          if ( yGrid, xGrid ) in pixel:
            v += 1
          v *= 2
      if v in algorithm:
        newPixel[ ( l, c)] = 1
  return newPixel

def printGrid( grid):
  minX =  minY = 1000 
  maxX =  maxY = -1000
  for (y,x) in grid:
    minX = min( minX, x)
    minY = min( minY, y)
    maxX = max( maxX, x)
    maxY = max( maxY, y)
  for y_ in range( minX, maxX + 1):
    for x_ in range( minY, maxX + 1):
      if  ( y_, x_) in grid:
        print( "#", end = '')
      else: 
        print( ".", end='')
    print()

p = process( pixel)
printGrid( p)
p = process( p)
print()
printGrid( p)
print( len(p))
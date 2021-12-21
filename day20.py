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

def process( oldGrid, x0, y0, w, h, loops):
  for l in range( loops):
    newPixel = {}
    ymin = y0 - l - 1
    ymax = y0 + h + l
    xmin = x0 - l - 1
    xmax = x0 + w + l
    isEvenLoop = True if l // 2 == (l + 1) // 2 else False
    for y in range( ymin, ymax + 1):
      for x in range( xmin, xmax + 1):
        v = 0
        for yGrid in range( y - 1, y + 2):
          for xGrid in range( x - 1, x + 2):
            if ( yGrid, xGrid ) in oldGrid or (not isEvenLoop and ( yGrid <= ymin or yGrid >= ymax  or xGrid <= xmin or xGrid >= xmax )):
              v += 1
            v *= 2
        v //= 2
        if v in algorithm:
          newPixel[ ( y, x)] = 1
    oldGrid = newPixel.copy()
  return newPixel

# for debugging
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
  print( minY, maxY, minX, maxX)

# Task 1

p = process( pixel, 0, 0, width, height, 2)
print( "Result Task 1: ", len(p))

# Task 2

p = process( pixel, 0, 0, width, height, 50)
print( "Result Task 2: ", len(p))


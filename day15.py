# AdventOfCode 2021
# Day 15

#get input data

import sys, random
sys.setrecursionlimit( 3000)

lines = []
with open( "15.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

gridSizeY = len(lines)
gridSizeX = len( lines[0])
grid = []
for l in lines:
    x = [ int(i) for i in list( l)]
    grid.append( x)

def getInitialMinRisk( grid):
  return len(grid) * len(grid[0]) * 9

def walk( x, y, risk):
  global minRisk
  path[ ( x, y)] = ''
  risk += grid[ y][ x]
  if risk >= minRisk:
    return 
  if not ( x, y) in riskGrid:
    riskGrid[ ( x, y)] = risk
  else:
    if riskGrid[ ( x, y)] > risk:
      riskGrid[ (x, y)] = risk
    else:
      return
  if x == gridSizeX - 1 and y == gridSizeY - 1:
    if risk < minRisk:
      minRisk = risk
      print( "new minimal risk found: ", minRisk)
    return
  if (x + 1, y) not in path and x < gridSizeX - 1:
    walk( x + 1, y, risk)
    path.popitem()
  if (x, y + 1) not in path and y < gridSizeY - 1:
    walk( x, y + 1, risk)
    path.popitem()
  if (x - 1, y) not in path and x > 0:
    walk( x - 1, y, risk)
    path.popitem()
  if (x, y - 1) not in path and y > 0:
    walk( x, y - 1, risk)
    path.popitem()

#Task 1

riskGrid = {} 
path = {}
minRisk = getInitialMinRisk( grid)
import time
start = time.time()
walk( 0, 0, 0)
end = time.time()

print( "Result Task 1: ", minRisk - grid[0][0])
print( end - start)
exit()

#Task 2

def buildLargeGrid( grid, mult):
  for i in range( 1, mult):
    for y in range( gridSizeY):
       for x in range( gridSizeX):
         v = grid[ y][ x] + i
         grid[y].append( v - 9 if v > 9 else v)
  newGridSizeX = len( grid[ 0])
  for i in range( 1, mult):
    for y in range( gridSizeY):
      grid.append([])
      for x in range( newGridSizeX):
        v = grid[ y][ x] + i
        grid[-1].append( v - 9 if v > 9 else v)
  return grid

grid = buildLargeGrid( grid, 5)
gridSizeY = len( grid)
gridSizeX = len( grid[0])

riskGrid = {} 
path = {}
minRisk = getInitialMinRisk( grid)
walk( 0, 0, 0)

print( "Result Task 2: ", minRisk - grid[0][0])

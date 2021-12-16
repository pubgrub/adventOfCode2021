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
      #print( "new minimal risk found: ", minRisk)
      print( ".", end='')
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

def solve( grid):
  toCalc[ ( 1, 0)] = ''
  toCalc[ ( 0, 1)] = ''
  while len(toCalc) != 0:
    ( x, y) =  next(iter(toCalc)) 
    neighbors = []
    if x > 0:
      neighbors.append( (x-1, y))
    if x < gridSizeX - 1:
      neighbors.append( (x+1, y))
    if y > 0:
      neighbors.append( (x, y-1))
    if y < gridSizeY - 1:
      neighbors.append( (x, y+1))
      
    minRiskOfNeighbors = maxRisk
    #print( x, y, neighbors, len( toCalc))
    for (xn, yn) in neighbors:

      if ( xn, yn) in minPointRisks:
        minRiskOfNeighbors = min( minRiskOfNeighbors, minPointRisks[ ( xn, yn)])
    if ( x, y) not in minPointRisks or minRiskOfNeighbors < minPointRisks[ ( x, y)] - grid[y][x]:
      #print( x, y)
      minPointRisks[ ( x, y)] = minRiskOfNeighbors + grid[y][x]
      for n in neighbors:
        ( xn, yn) = n
        if not n in minPointRisks or minPointRisks[ ( x, y)] + grid[ yn][ xn] < minPointRisks[ xn, yn]:
          toCalc[ n] = ''
    toCalc.pop( ( x, y))

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


import time
#Task 1

minPointRisks = { ( 0,0): 0}
toCalc = {}
maxRisk = getInitialMinRisk(grid)
minRisk = maxRisk

riskGrid = {} 
path = {}

# slowVersion
#walk( 0, 0, 0)
#print( "Result Task 1: ", minRisk - grid[0][0])

# fastVersion

start1 = time.time()
solve( grid)
end1 = time.time()
print( minPointRisks[ ( gridSizeX - 1, gridSizeY - 1)])
print( end1 -start1)
#Task 2

grid = buildLargeGrid( grid, 5)
gridSizeY = len( grid)
gridSizeX = len( grid[0])

minPointRisks = { ( 0,0): 0}
toCalc = {}
maxRisk = getInitialMinRisk(grid)
minRisk = maxRisk

riskGrid = {} 
path = {}

start2 = time.time()
solve( grid)
end2 = time.time()

print( minPointRisks[ ( gridSizeX - 1, gridSizeY - 1)])
print( end2 - start2)


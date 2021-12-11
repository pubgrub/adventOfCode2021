# AdventOfCode 2021
# Day 11

#get input data

lines = []
with open( "11.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

#grid has -1 around to test neighbors for border
bordererdGrid = [ -1] * 12
for l in lines:
  bordererdGrid.append( -1)
  bordererdGrid = bordererdGrid + [int(x) for x in list(l)]
  bordererdGrid.append( -1)
bordererdGrid = bordererdGrid +  [ -1] * 12

neighors = [ -13, -12, -11, -1, 1, 11, 12, 13]

#print function for testing
def printGrid( grid):
  print( "\033[0m")
  for i in range(1,11):
    for j in range(1,11):
      val = grid[ i * 12 + j]
      valstr = "{0:3d}".format( val)
      if  val == 0:
        print( "\033[1;31m" + valstr + "\033[0m" , end = "")
      else:
        print( valstr, end = "")
    print( "\033[0m")

def raiseEnergy( oct, octs, has_flashed, flashCount):
  octs[ oct] += 1
  if octs[ oct] == 10:
    has_flashed.add( oct)
    octs[ oct] = 0
    flashCount += 1
    for n in neighors:
      neighborPos = oct + n
      if neighborPos < 0 or neighborPos >= len(octs) or octs[ neighborPos] == -1 or neighborPos in has_flashed:
          continue
      ( octs, has_flashed, flashCount) = raiseEnergy( neighborPos, octs, has_flashed, flashCount)
  return ( octs, has_flashed, flashCount)   

#Task 1

octs = bordererdGrid[:]
has_flashed = set()
flashCount = 0
steps = 100

for s in range( steps):
  has_flashed.clear()
  for o in range(len(octs)):
    if octs[ o]  == -1 or o in has_flashed:
      continue
    ( octs, has_flashed, flashCount) = raiseEnergy( o, octs, has_flashed, flashCount)

print( "Result Task 1: ", flashCount)

#Task 2

octs = bordererdGrid[:]

step = 0
while len(has_flashed) != 100:
  step += 1
  has_flashed.clear()
  for o in range(len(octs)):
    if octs[ o]  == -1 or o in has_flashed:
      continue
    ( octs, has_flashed, flashCount) = raiseEnergy( o, octs, has_flashed, flashCount)

print( "Result Task 2: ", step)

# AdventOfCode 2021
# Day 12

#get input data

lines = []
with open( "12.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

paths = []
for l in lines:
    paths.append( tuple(l.split('-')))

isMajor = [False, False]
destinations = [[], []]
sourceName = ['start', 'end']

for ( s, d) in paths:
  for p in [ s, d]:
    if p not in sourceName:
      sourceName.append( p)
      destinations.append( [])
      isMajor.append( True if p.upper() == p else False)
  destinations[ sourceName.index( s)].append( sourceName.index( d))
  destinations[ sourceName.index( d)].append( sourceName.index( s))

#Task 1

def walk1( dest, way, count):
  way = way.copy()
  if dest == 1:
    return count + 1
  way.append( dest)
  for d in destinations[ dest]:
    if d in way and not isMajor[ d]:
      continue
    else:
      count = walk1( d, way, count) 
  return count

count = walk1( 0, [], 0)

print( "Result Task 1: ", count)

#Task 2

def walk2( dest, way, count, minorVisited):
  if dest in way and not isMajor[ dest]:
    minorVisited = True
  way = way.copy()
  if dest == 1:
    return count + 1
  way.append( dest)
  for d in destinations[ dest]:
    if d == 0 or d in way and not isMajor[ d] and minorVisited:
        continue
    count = walk2( d, way, count, minorVisited) 
  return count

count = walk2( 0, [], 0, False)

print( "Result Task 2: ", count)

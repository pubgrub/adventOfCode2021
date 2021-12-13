# AdventOfCode 2021
# Day 12

#get input data

lines = []
with open( "12.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

connections = []
for l in lines:
    connections.append( tuple(l.split('-')))

isMajor = [False, False]
destinations = [[], []]
sourceName = ['start', 'end']

for ( s, d) in connections:
  for p in [ s, d]:
    if p not in sourceName:
      sourceName.append( p)
      destinations.append( [])
      isMajor.append( True if p.upper() == p else False)
  destinations[ sourceName.index( s)].append( sourceName.index( d))
  destinations[ sourceName.index( d)].append( sourceName.index( s))

#Task 1

def walk1( point, path, count):
  path = path.copy()
  if point == 1:
    return count + 1
  path.append( point)
  for d in destinations[ point]:
    if d in path and not isMajor[ d]:
      continue
    else:
      count = walk1( d, path, count) 
  return count

count = walk1( 0, [], 0)

print( "Result Task 1: ", count)

#Task 2

def walk2( point, path, count, minorVisited):
  if point in path and not isMajor[ point]:
    minorVisited = True
  path = path.copy()
  if point == 1:
    return count + 1
  path.append( point)
  for d in destinations[ point]:
    if d == 0 or d in path and not isMajor[ d] and minorVisited:
        continue
    count = walk2( d, path, count, minorVisited) 
  return count

count = walk2( 0, [], 0, False)

print( "Result Task 2: ", count)

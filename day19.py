# AdventOfCode 2021
# Day 19

#get input data

lines = []
with open( "19.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

scanner = -1
beacons = []
for l in lines:
  if len(l) == 0:
    continue
  elif l[:3] == '---':
    scanner += 1
    beacons.append([])
    beacons[ scanner] = [[], [], []]
  else:
    (x, y, z) = l.split( ',')
    beacons[ scanner][0].append( int(x))    
    beacons[ scanner][1].append( int(y))    
    beacons[ scanner][2].append( int(z))

SCANNERS = scanner + 1
XYZ = [ 0, 1, 2]
print( SCANNERS)
orientation = [1]
combDist = {}
i = 0
for s1 in range( SCANNERS):
  for s2 in range( s1 + 1, SCANNERS):
    for b1 in beacons[ s1]:
      for b2 in beacons[ s2]:
        for o in orientation:
          for d in XYZ:
            combDist[ b1[d] + b2[d]] = ( s1, s2, d, o) 
            i += 1
print( i)
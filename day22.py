# AdventOfCode 2021
# Day 22

#get input data

from operator import add

lines = []
with open( "22test.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())

#on x=-44..9,y=-9..44,z=-34..13

onOff1 = []
onOff2 = []
coords1 = []
coords2 = []
for l in lines:
  l = l.replace( ',y=', '..').replace( ',z=', '..')
  onOffStr, coord = l.split(' x=')
  xmin, xmax, ymin, ymax, zmin, zmax = [ int(x) for x  in coord.split( '..')]
  if xmin >= -50 and xmin <= 50:
    onOff1.append( 1 if onOffStr == 'on' else 0)
    coords1.append( ( xmin, xmax, ymin, ymax, zmin, zmax))
  else:
    onOff2.append( 1 if onOffStr == 'on' else 0)
    coords2.append( ( xmin, xmax, ymin, ymax, zmin, zmax))

# Task 1

cubes = {}
for i in range( len(coords1)):
  ( xmin, xmax, ymin, ymax, zmin, zmax) = coords1[ i]
  for x in range( xmin, xmax + 1):
    for y in range( ymin, ymax + 1):
      for z in range( zmin, zmax + 1):
        if onOff1[ i]:
          cubes[ ( x, y, z)] = 1
        else:
          cubes.pop( ( x, y, z), 0)

result1 = len(cubes)
print( "Result Task 1: ", result1)

# Task 2

class Point:
  def __init__( self, x, y, z):
    self.xyz = [ x, y, z]

  def __repr__( self):
    return( f'Point: ({self.xyz[0]}, {self.xyz[1]}, {self.xyz[2]}) ')

  def getXYZ( self):
    return( self.x, self.y, self.z)

class Edge:
  def __init__( self, point1, point2):
    self.points = [ point1, point2]
    for i, k in enumerate( point1.xyz):
      if k != point2.xyz[i]:
        self.axis = i
        self.dir = 1 if point2.xyz[i] > k else -1
        break

  def __repr__(self):
    return f'Edge: {self.points[0]}, {self.points[1]}, Axis: {self.axis}, Direction: {self.dir}\n'

class Face:
  def __init__( self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def __repr__(self):
    return f'Face: {self.point1}, {self.point2}\n'


class Cube:
  def __init__( self, *args):
    if len( args) == 3:
      self.points = [ args[0], args[1]]
      self.onOff = args[ 2]
    if len( args) == 7:
      self.points = [ Point( args[0], args[1], args[2]), Point( args[3], args[4], args[5])]
      self.onOff = args[6]
    self.allPoints, self.edges, self.faces = self.calcGeometries()

  def __str__(self) -> str:
      return( f'Cube ( {[p for p in self.points]}) , onOff: {self.onOff}' )

  def __repr__( self):
    return( self.__str__())

  def calcGeometries( self):
    allPoints = []
    for x in [ self.points[0].xyz[0], self.points[1].xyz[0]]:
      for y in [ self.points[0].xyz[1], self.points[1].xyz[1]]:
        for z in [ self.points[0].xyz[2], self.points[1].xyz[2]]:
          allPoints.append( Point( x, y, z))
    edges = []
    faces = []
    for p1 in range( len(allPoints) -1):
      for p2 in range( p1 +1 , len( allPoints)):
        ortho = 0
        for k in range( 3):
          if allPoints[p1].xyz[k] == allPoints[p2].xyz[k]:
            ortho += 1
        if ortho == 2:
          edges.append( Edge( allPoints[p1], allPoints[p2]))
        if ortho == 1 and (p1 == 0 or p2 == len( allPoints) -1):
          faces.append( Face( allPoints[p1], allPoints[p2]))
    return (allPoints, edges, faces)   

  def isPointInside( self, p):
    for k in range( 3):
      if p.xyz[k] < self.points[0].xyz[k] or p.xyz[k] > self.points[1].xyz[k]:
        return False
    return True


coords2 = coords1.copy()
onOff2 = onOff1.copy()
cubes = ()
for c in range( len( coords2)):

  cubes +=  ( [Cube(  *[x for x in coords2[c]] + [onOff2[c]] ) , c ],  )

for c in cubes:
  print( c)
  print( c.__class__)
  for cc in c:
    print( cc)
    print( cc.__class__)

  #print( cubes)

newCubes = []

for c1, order1 in cubes:
  for c2, order2 in cubes:
    if c1 is c2:
      continue
    else:
      for e in c1.edges:
        for p in e.points:
          if c2.isPointInside( p):
            axis = e.axis
            dir = e.dir
            
            




# with layers??
# layers = {}
# for cube in range( len(coords2)):
#   xmin, xmax, ymin, ymax, zmin, zmax = coords2[ i]
#   for z in range( zmin, zmax + 1):
#     if not z in layers:
#       layers[ z] = []
#     layers[ z].append( ( xmin, xmax, ymin, ymax, onOff2[ cube]))
# print( len( layers))
# maxl = 0
# for l in layers:
#   maxl = max( maxl, len( layers[ l]))
# print( maxl)


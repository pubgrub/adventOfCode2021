# AdventOfCode 2021
# Day 22

#get input data

from operator import add

lines = []
with open( "22.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

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
        self.x = x
        self.y = y
        self.z = z
class Edge:
    def __init__( self, point1, point2):
        self.point1 = point1
        self.point2 = point2
class Face:
    def __init__( self, point1, point2):
        self.point1 = point1
        self.point2 = point2

class Cube:
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax, onOff):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.onOff = onOff

    def getAllEdges( self):
        points = []
        for x in [ self.xmin, self.xmax]:
            for y in [ self.ymin, self.ymax]:
                for z in [ self.zmin, self.zmax]:
                    points.append( Point( x, y, z))
        edges = []
        for i in range( len(points)):
            for j in range( i, len( points)):
                

        result = []
        result.append( )

def hasIntersection( ( x1, x2, y1, y2), ( z1, z2)):





# with layers??
# layers = {}
# for cube in range( len(coords2)):
#     xmin, xmax, ymin, ymax, zmin, zmax = coords2[ i]
#     for z in range( zmin, zmax + 1):
#         if not z in layers:
#             layers[ z] = []
#         layers[ z].append( ( xmin, xmax, ymin, ymax, onOff2[ cube]))
# print( len( layers))
# maxl = 0
# for l in layers:
#     maxl = max( maxl, len( layers[ l]))
# print( maxl)


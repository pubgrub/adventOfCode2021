# AdventOfCode 2021
# Day 5

#get input data

lines = []
with open( "05.data", "r") as file:
  for line in file:
    lines.append( line.rstrip().replace(' -> ', ','))
file.close()

class Vent:

    def __init__(self, coordString):
        [self.x1, self.y1, self.x2, self.y2] = [int(x) for x in coordString.split(',')]

    def getAllPoints(self):
        if self.isHorizontal():
            return( [(x, self.y1) for x in range( min( self.x1, self.x2), max(self.x1, self.x2 ) +1)])
        if self.isVertical():
            return( [(self.x1, y) for y in range( min( self.y1, self.y2), max(self.y1, self.y2 ) +1)])
        else:
            xrange = range( self.x1, self.x2 +1, 1) if self.x2 > self.x1 else range( self.x1, self.x2 - 1, -1)
            yrange = range( self.y1, self.y2 +1, 1) if self.y2 > self.y1 else range( self.y1, self.y2 - 1, -1)
            l =  []
            for i in range( 0, len(xrange)):
                l.append( (xrange[i], yrange[i]))
            return l

    def isHorizontal(self):
        return( self.y1 == self.y2)

    def isVertical(self):
        return( self.x1 == self.x2)

#Task 1:

vents = []
for l in lines:
    vents.append( Vent(l))

grid = {}
for v in vents:
    if v.isHorizontal() or v.isVertical():
        for p in v.getAllPoints():
            try:
                grid[ p] += 1
            except KeyError:
                grid[p] = 1

result = 0
for key in grid:
    if grid[key] > 1:
        result += 1

print( "Result Task 1: ", result)

#Task 2:

vents = []
for l in lines:
    vents.append( Vent(l))

grid = {}
for v in vents:
    for p in v.getAllPoints():
        try:
            grid[ p] += 1
        except KeyError:
            grid[p] = 1

result = 0
for key in grid:
    if grid[key] > 1:
        result += 1

print( "Result Task 2: ", result)


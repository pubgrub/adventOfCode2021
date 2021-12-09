# AdventOfCode 2021
# Day 9

#get input data

lines = []
with open( "09.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

heights = []
for l in lines:
    heights.append(  [ int(x) for x in list(l)])

#Task 1

risk = 0
lowPoints = []
for l in range( 0, len(heights)):
    for h in range( 0, len( heights[l])):
        height = heights[l][h]
        if l > 0 and heights[ l - 1][ h] <= height:
            continue
        if l < len( heights) - 1 and heights[ l + 1][h] <= height:
            continue
        if h > 0 and heights[ l][h - 1] <= height:
            continue
        if h < len(heights[l]) - 1 and heights[l][ h + 1] <= height:
            continue
        #remember for task 2
        lowPoints.append( ( h, l))
        risk = risk + height + 1

print( "Result Task 1: ", risk)

#Task 2

maxY = len(heights) - 1
maxX = len( heights[0]) - 1

def find_lowArea(  xy, areaPoints):
    ( x, y) = xy
    areaPoints.append( xy)
    neighbors = []
    if x > 0 and heights[y][ x - 1] < 9:
        neighbors.append( ( x - 1, y))
    if x < maxX and heights[ y][ x + 1] < 9:
        neighbors.append( ( x + 1, y))
    if y > 0 and heights[y - 1][ x] < 9:
        neighbors.append( ( x, y - 1))
    if y < maxY and heights[y + 1][ x] < 9:
        neighbors.append( ( x, y + 1))
    for n in neighbors:
        if n not in areaPoints:
            areaPoints = find_lowArea( n, areaPoints)
    return areaPoints

lowAreas = [ len(find_lowArea( x, []))  for x in lowPoints ]
lowAreas.sort()
lowAreas.reverse()
result = lowAreas[ 0] * lowAreas[ 1] * lowAreas[ 2]

print( "Result Task 2: ", result)

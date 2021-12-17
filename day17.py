# AdventOfCode 2021
# Day 17

#get input data

lines = []
with open( "17.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

(dummy, xRange, yRange) = lines[0].replace( ', ', ': ').replace('=', '..').split( ': ')
(dummy, targetXMin, targetXMax) = xRange.split( '..')
(dummy, targetYMin, targetYMax) = yRange.split( '..')

targetXMin, targetXMax, targetYMin, targetYMax = [ int(x) for x in [ targetXMin, targetXMax, targetYMin, targetYMax]]

minPossXVel0 = int( ((1 + 8 * targetXMin) ** 0.5 -1) // 2)  # Gauss inverted
maxPossXVel0 = targetXMax
minPossYVel0 = targetYMin
maxPossYVel0 = abs(targetYMin)

#Task 1 + 2

bestY = 0
solutions = 0
for yVel0 in range( minPossYVel0, maxPossYVel0 + 1):
    for xVel0 in range( minPossXVel0, maxPossXVel0 + 1):
        y = x = 0
        xVel = xVel0
        yVel = yVel0
        bestLocalY = 0
        while True:
            x += xVel
            y += yVel
            bestLocalY = max( bestLocalY, y)
            xVel = max( 0, xVel - 1)
            yVel -= 1
            if x > targetXMax or y < targetYMin:
                break
            if x >= targetXMin and x <= targetXMax and y >= targetYMin and y <= targetYMax:
                # in Target
                solutions += 1
                bestY = max( bestY, bestLocalY)
                break

print( "Result Task 1: ", bestY)
print( "Result Task 2: ", solutions)

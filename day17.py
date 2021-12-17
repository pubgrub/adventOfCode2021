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

yVel0 = minPossYVel0 - 1
bestY = 0
solutions = 0
while True:
    yVel0 += 1
    if yVel0 > maxPossYVel0:
        break
    xVel0 = minPossXVel0
    while True:
        xVel0 += 1
        if xVel0 > maxPossXVel0:
            break
        y = x = 0
        xVel = xVel0
        yVel = yVel0
        bestLocalY = 0
        while True:
            x += xVel
            y += yVel
            if y > bestLocalY:
                bestLocalY = y
            xVel = max( 0, xVel - 1)
            yVel -= 1
            if x > targetXMax or y < targetYMin:
                break
            if x >= targetXMin and x <= targetXMax and y >= targetYMin and y <= targetYMax:
                # in Target
                solutions += 1
                if bestLocalY > bestY:
                    bestY = bestLocalY
                break

print( "Result Task 1: ", bestY)
print( "Result Task 2: ", solutions)

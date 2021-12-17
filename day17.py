# AdventOfCode 2021
# Day 17

#get input data

lines = []
with open( "17.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

(dummy, targetXMin, targetXMax, dummy, targetYMin, targetYMax) = lines[0].replace( ', ', '..').replace('=', '..').split( '..')
targetXMin, targetXMax, targetYMin, targetYMax = [ int(x) for x in [ targetXMin, targetXMax, targetYMin, targetYMax]]

vX0min = int((( 8 * targetXMin + 1) ** 0.5 - 1) // 2)  # Gauss inverted
vX0max = targetXMax
vY0min = targetYMin
vY0max = abs(targetYMin)

#Task 1 + 2

bestY = 0
solutions = 0
for vY0 in range( vY0min, vY0max + 1):
    for vX0 in range( vX0min, vX0max + 1):
        y = x = 0
        vX = vX0
        vY = vY0
        bestLocalY = 0
        while True:
            x += vX
            y += vY
            bestLocalY = max( bestLocalY, y)
            vX = max( 0, vX - 1)
            vY -= 1
            if x > targetXMax or y < targetYMin:
                break
            if x >= targetXMin and x <= targetXMax and y >= targetYMin and y <= targetYMax:
                # in Target
                solutions += 1
                bestY = max( bestY, bestLocalY)
                break

print( "Result Task 1: ", bestY)
print( "Result Task 2: ", solutions)

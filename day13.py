# AdventOfCode 2021
# Day 13

#get input data

lines = []
with open( "13.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

dots = []
fold = []
for l in lines:
    if ',' in l:
        dots.append( tuple( int( x) for x in l.split(',')))
    if '=' in l:
        (dummy, dummy, foldInstruction) = l.split( ' ')
        ( foldDir, foldVal) = foldInstruction.split( '=')
        fold.append( ( foldDir, int( foldVal)))

def doFold( dots, foldDir, foldVal):
    newDots = dots.copy()
    for (x, y) in dots:
        if foldDir == 'y' and y > foldVal:
            newDots.remove( ( x, y))
            newY = -y + foldVal * 2
            if not ( x, newY) in dots:
                newDots.append( ( x, newY))
        elif foldDir == 'x' and x > foldVal:
            newDots.remove( ( x, y))
            newX = -x + foldVal * 2
            if not ( newX, y) in dots:
                newDots.append( ( newX, y))
    return newDots

def generateMatrix( dots):
    maxX = maxY = 0
    lines = []
    for ( x, y) in dots:
        maxX = max( maxX, x)
        maxY = max( maxY, y)
    for y in range( maxY+ 1):
        str = ''
        for x in range( maxX + 1):
            str += "O" if ( x, y) in dots else " "
        lines.append( str)
    return lines

#Task 1

(foldDir , foldVal) = fold[ 0]
newDots = doFold( dots, foldDir, foldVal)

print( "Result Task 1: ", len( newDots))

#Task 2

for (foldDir, foldVal) in fold:
    dots = doFold( dots, foldDir, foldVal)

print( "Result Task 2: \n")
for l in generateMatrix( dots):
    print( l)
print()
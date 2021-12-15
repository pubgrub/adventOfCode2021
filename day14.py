# AdventOfCode 2021
# Day 14

#get input data

lines = []
with open( "14.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

primer = list( lines[0])

insertions = {}
insertions2 = {}
for l in lines[ 2:]:
    ( pair, ins) = l.split( ' -> ') 
    (x, y) = list( pair)
    insertions[ (x, y)]= ins
    insertions2[ pair] = ins

def polymerToStr( poly, next):
    str = ""
    i = 0
    while i != -1:
        str += poly[ i] + " "
        i = next[ i]
    return str        



def getPolymerSlow( polymer, steps):
    nextPiece = []
    for i in range( len(primer) - 1):
        nextPiece.append(  i + 1)
    nextPiece.append( -1)

    tempP = polymer.copy()
    tempN = nextPiece.copy()
    for s in range( steps):
        print( "STep: ", s)
        for p in range( len( polymer)):
            if nextPiece[ p] == -1:
                continue
            actPiece = polymer[ p]
            rightPiece = polymer[ nextPiece[ p]]
            if ( actPiece, rightPiece) in insertions:
                tempP.append( insertions[ ( actPiece, rightPiece)])
                nextPiece.append(  nextPiece[ p])
                nextPiece[ p] = len( tempP)- 1
        polymer = tempP.copy()
    return polymer

def getCounts( polymer):
    count = {}
    for i in polymer:
        count[ i] = count.get( i, 0) + 1
    minC = maxC = 0
    for c in count.values():
        minC = c if minC == 0 else min( minC, c)
        maxC = max( maxC, c)
    return( ( minC, maxC))

#Task 1

polymer = getPolymerSlow( primer, 10)
( minC, maxC) = getCounts( polymer)

print( "Result Task 1: ", maxC - minC)

#Task 2

# polymer = getPolymerSlow( primer, 40)
# ( minC, maxC) = getCounts( polymer)

# print( "Result Task 2: ", maxC - minC)

results = {}
for i in insertions2:
    results[ ( i)] = i[0] + insertions2[i] + i[1]




#print( insertions2)
print( results)

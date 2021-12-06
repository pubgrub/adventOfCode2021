# AdventOfCode 2021
# Day 6

#get input data

lines = []
with open( "06.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

fish = [int(x) for x in lines[0].split(',')]

wait = [0 ] * 9
for f in fish:
    wait[ f] += 1

def slowCalc( fish, days):
    fishList = fish[:]
    for d in range( 0, days):
        newList = []
        for f in range( len(fishList)):
            if fishList[ f] == 0:
                fishList[ f] = 6
                newList.append( 8)
            else:    
                fishList[ f] -= 1
        fishList.extend( newList)
    return ( len(fishList))

def fastcalc( w, days):
    wait = w[:]
    for d in range( days):
        newFish = wait[0]
        for i in range( 1, 9):
            wait[ i-1] = wait[ i]
        wait[ 8] = newFish
        wait[ 6] += newFish
    return( sum( wait))

#Task 1:

#print( "Result Task 1: " , slowCalc( fish, 80))
print( "Result Task 1: ", fastcalc( wait, 80))

#Task 2:

#print( "Result Task 1: " , slowCalc( fish, 256))
print( "Result Task 2: ", fastcalc( wait, 256))

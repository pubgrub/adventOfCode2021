# AdventOfCode 2021
# Day 7

#get input data

lines = []
with open( "07.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

fishPos = [int( x) for x in lines[0].split( ',')]
minpos = min( fishPos)
maxpos = max( fishPos)

#Task 1

def find_best( minp, maxp, f):
    mid = int( (minp + maxp) / 2)
    fuel = calc_fuel( mid, f)
    fuel_left = calc_fuel( mid - 1, f)
    fuel_right = calc_fuel( mid + 1, f)
    #print( minp, maxp, mid, fuel, fuel_left, fuel_right)
    if fuel_left < fuel:
        fuel = find_best( minp, mid - 1, f)
    elif fuel_right < fuel:
        fuel = find_best( mid + 1, maxp, f)        
    return( fuel)

def calc_fuel( aktpos, f):
    fuel = 0
    for p in fishPos:
        fuel += f( aktpos, p) 
    return fuel

minfuel = 0
for i in range( minpos, maxpos  + 1):
    fuel = 0
    for p in fishPos:
        fuel += abs( i - p)
    if  minfuel == 0:
        minfuel = fuel
    elif fuel < minfuel:
        minfuel = fuel

print( "Slow Result Task 1: ", minfuel)

f1 = lambda x, y: abs( y - x)
print( "Faster result Task 1: ", find_best( minpos, maxpos, f1))

#Task 2

minfuel = 0
for i in range( minpos, maxpos  + 1):
    fuel = 0
    for p in fishPos:
        a = abs( i - p)
        fuel += int( (a**2 + a) / 2)
    minfuel = min( minfuel, fuel)  if minfuel else fuel
print( "Slow Result Task 2: ", minfuel)

f2 = lambda x, y: int(   (abs( x - y)**2 + abs( x - y)) / 2 )
print( "Faster result Task 2: ", find_best( minpos, maxpos, f2))

# AdventOfCode 2021
# Day 7

#get input data

lines = []
with open( "07.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

pos = [int( x) for x in lines[0].split( ',')]
minpos = min( pos)
maxpos = max( pos)

#Task 1

minfuel = 0
for i in range( minpos, maxpos  + 1):
    fuel = 0
    for p in pos:
        fuel += abs( i - p)
    minfuel = min( minfuel, fuel)  if minfuel else fuel

print( "Result Task 1: ", minfuel)

#Task 2

minfuel = 0
for i in range( minpos, maxpos  + 1):
    fuel = 0
    for p in pos:
        a = abs( i - p)
        fuel += int( (a**2 + a) / 2)
    minfuel = min( minfuel, fuel)  if minfuel else fuel

print( "Result Task 2: ", minfuel)

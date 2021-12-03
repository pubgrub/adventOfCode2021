# AdventOfCode 2021
# Day 1

#get input data
depths = []
with open( "01.data", "r") as file:
    for line in file:
        depths.append( int(line))
file.close()

#Task 1
result = 0
for i in range( 1,len(depths)):
    if depths[i] > depths[i-1]:
        result += 1
print( "Result Task 1: " , result)

#Task 2
result = 0
lasttriple = 0
for i in range( 0,len(depths)-2):
    triple = depths[i] + depths[i+1] + depths[ i+2]
    if triple > lasttriple and i > 0:
        result += 1
    lasttriple = triple 
print( "Result Task 2: " , result)

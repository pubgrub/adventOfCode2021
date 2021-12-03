# AdventOfCode 2021
# Day 2

#get input data
command = []
commandvalue = []
with open( "02.data", "r") as file:
    for line in file:
        (c, v) = line.split( " ")
        command.append( c)
        commandvalue.append( int(v))
file.close()

#Task 1
x = 0
depth = 0
for i in range( 0,len(command)):
    if command[ i] == "forward":
        x += commandvalue[ i]
    elif command[ i] == "up":
        depth -= commandvalue[ i]
    elif command[ i] == "down":
        depth += commandvalue[ i]

print( "Result Task 1: forward: " , x, "down: ", depth, "solution: ", x * depth)

#Task 2
aim = 0
x = 0
depth = 0
for i in range( 0,len(command)):
    if command[ i] == "forward":
        x += commandvalue[ i]
        depth += commandvalue[i] * aim
    elif command[ i] == "up":
        aim -= commandvalue[ i]
    elif command[ i] == "down":
        aim += commandvalue[ i]
print( "Result Task 2: forward: " , x, "down: ", depth, "solution: ", x * depth)

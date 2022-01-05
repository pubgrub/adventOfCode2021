# AdventOfCode 2021
# Day 25

#get input data

lines = []
with open( "25.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())

y_size = len(lines)
x_size = len(lines[0])

down = {}
right = {}
for y, l in enumerate(lines):
    for x, c in enumerate( list(l)):
#        print( y, x, c)
        if c == 'v':
            down[( x, y)] = 1
        if c == '>':
            right[( x, y)] = 1

def print_grid():
    for y in range( y_size):
        s = ''
        for x in range( x_size):
            if ( x, y) in right:
                s += '>'
            elif ( x, y) in down:
                s += 'v'
            else:
                s += '.'
        print( s)


moved = True
steps = 0
while moved:
    moved = False
    new_down = {}
    new_right = {}
    del_down = {}
    del_right = {}
    
    for ( x, y) in right:
        if x != x_size - 1:
            if not ( x + 1, y) in right and not ( x + 1, y) in down:
                del_right[ ( x, y)] = 1
                new_right[ ( x + 1, y)] = 1
        else:
            if not ( 0, y) in right and not ( 0, y) in down:
                del_right[ ( x, y)] = 1
                new_right[ ( 0, y)] = 1
    if new_right:
        moved = True
        for n in del_right:
            right.pop( n)
        for n in new_right:
            right[ n] = 1

    for ( x, y) in down:
        if y != y_size - 1:
            if not ( x, y + 1) in right and not ( x, y + 1) in down:
                del_down[ ( x, y)] = 1
                new_down[ ( x, y + 1)] = 1
        else:
            if not ( x, 0) in right and not ( x, 0) in down:
                del_down[ ( x, y)] = 1
                new_down[ ( x, 0)] = 1
    if new_down:
        moved = True
        for n in del_down:
            down.pop( n)
        for n in new_down:
            down[ n] = 1

    if moved:
        steps += 1

print( "Result Task 1: ", steps + 1)

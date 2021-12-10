# AdventOfCode 2021
# Day 10

#get input data

lines = []
with open( "10.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

openBrackets = [ '(', '[', '{', '<']
closeBrackets = [ ')', ']', '}', '>']

# Task 1

corruptionValue = [ 3, 57, 1197, 25137]
score = 0
remainingStacks = []
for l in lines:
    stack = []
    corrupted = False
    for c in l:
        if c in openBrackets:
            stack.append( c)
        else:
            if len( stack) == 0 or stack[ -1] != openBrackets[ closeBrackets.index( c)]:
                score += corruptionValue[ closeBrackets.index( c)]
                corrupted = True
                break
            else:
                stack.pop()
    if len( stack) > 0 and corrupted == False:
        # remember for task 2
        remainingStacks.append( stack)

print( "Result Task 1: ", score)

# Task 2

scores = []
for s in remainingStacks:
    score = 0
    for c in s[ ::-1]:
        score = 5 * score + openBrackets.index( c) + 1
    scores.append( score)
scores.sort()
score = scores[ int( len( scores) / 2)]

print( "Result Task 1: ", score)

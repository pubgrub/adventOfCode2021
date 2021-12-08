# AdventOfCode 2021
# Day 8

#get input data

lines = []
with open( "08.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

digits = []
display = []
for  l in lines:
    s1, s2 = l.split( '|')
    digits.append( s1)
    display.append( s2)

#Task 1

count = { 2 : 0, 3 : 0, 4 : 0, 7 : 0}
for d in display:
    segments = d[1:].split( ' ')
    for s in segments:
        if len( s) in count:
            count[ len( s)] += 1
result = sum( [ x for x in count.values()]) 

print( "Result Task 1: ", result)

#Task 2

segToNum = [ 'ABCEFG', 'CF', 'ACDEG', 'ACDFG', 'BCDF', 'ABDFG', 'ABDEFG', 'ACF', 'ABCDEFG', 'ABCDFG']

sum = 0
for d in range( 0,len( digits)):
    hints = {}
    sets = []
    dlist = digits[d].split()
    dlist.sort( key = len)
    for dl in dlist:
        sets.append( set(list(dl)))
    hints[ 'A'] = sets[1] - sets[0]
    for s in [ x for x in sets[3:6]]:
        if sets[ 0].issubset( s):
            # 3
            hints[ 'G'] = s - sets[ 2]- hints[ 'A']
            hints[ 'D'] = s - sets[0] - hints[ 'A'] - hints[ 'G']
            hints[ 'B'] = sets[ 2] - sets[ 0]- hints[ 'D']
            hints[ 'E'] = sets[ 9] - s - hints[ 'B']
            break
    for s in [ x for x in sets[3:6]]:
        if hints[ 'B'].issubset( s):
            # 5
            hints[ 'F'] = s - hints[ 'B'] - hints[ 'A'] - hints[ 'D'] - hints[ 'G']
            hints[ 'C'] = sets[ 0] - hints[ 'F']
            break
    nums = []
    for n in range( 0, len(segToNum)):
        segs = ''
        for c in segToNum[ n]:
            segs += next(iter(hints[ c]))
        segs = ''.join(sorted(segs))
        nums.append( segs)
    ds = [ ''.join(sorted(x)) for x in display[d][1:].split( ' ')]
    n = 1000
    z = 0
    for digit in ds:
        z += nums.index( digit) * n
        n /=10
    sum += z
print( "Result Task 2: ", sum)    
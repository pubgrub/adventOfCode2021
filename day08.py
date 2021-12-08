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
    #decode wrong signals
    signal = {}
    sets = []
    dlist = digits[d].split()
    dlist.sort( key = len)
    for dl in dlist:
        sets.append( set(list(dl)))
    signal[ 'A'] = sets[1] - sets[0]
    for s in [ x for x in sets[3:6]]:
        if sets[ 0].issubset( s):
            # 3
            signal[ 'G'] = s - sets[ 2]- signal[ 'A']
            signal[ 'D'] = s - sets[0] - signal[ 'A'] - signal[ 'G']
            signal[ 'B'] = sets[ 2] - sets[ 0] - signal[ 'D']
            signal[ 'E'] = sets[ 9] - s - signal[ 'B']
            break
    for s in [ x for x in sets[3:6]]:
        if signal[ 'B'].issubset( s):
            # 5
            signal[ 'F'] = s - signal[ 'B'] - signal[ 'A'] - signal[ 'D'] - signal[ 'G']
            signal[ 'C'] = sets[ 0] - signal[ 'F']
            break
    
    # encode signals to digits
    signalCode = []
    for n in range( 0, len(segToNum)):
        segs = ''
        for c in segToNum[ n]:
            segs += next(iter(signal[ c]))
        segs = ''.join(sorted(segs))
        signalCode.append( segs)
    
    #  find digits for outputs and add numbers for result
    digitCodes = [ ''.join(sorted(x)) for x in display[d][1:].split( ' ')]
    multiplier = 1000
    result = 0
    for code in digitCodes:
        result += signalCode.index( code) * multiplier
        multiplier /=10
    sum += result

print( "Result Task 2: ", int( sum)    )
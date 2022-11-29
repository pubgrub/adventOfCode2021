# AdventOfCode 2021
# Day 14

#get input data

lines = []
with open( "14.data", "r") as file:
    for line in file:
        lines.append( line.rstrip())
file.close()

primer = lines[0]

def solve( runs):
    pairs = []
    subst = {}
    insertChar = {}
    charCount = {}

    # make substitute table
    for l in lines[ 2:]:
        ( pair, ins) = l.split( ' -> ') 
        (x, y) = list( pair)
        subst[pair] = [ x + ins, ins + y]
        insertChar[pair] = ins

    # load primer
    orig_pairs = {}
    dest_pairs = {}
    for i in range( len(primer) - 1):
        if not primer[ i:i+2] in orig_pairs:
            orig_pairs[ primer[i:i+2]] = 1
        else:
            orig_pairs[ primer[i:i+2]] += 1
    for i in range( len(primer)):
        if not primer[i] in charCount:
            charCount[primer[i]] = 1
        else:
            charCount[primer[i]] += 1

    #run
    for r in range(runs):
        for i in orig_pairs:
            for sub in subst[ i]:
                if not sub in dest_pairs:
                    dest_pairs[sub] = orig_pairs[i]
                else:
                    dest_pairs[sub] += orig_pairs[i]
            if not insertChar[i] in charCount:
                charCount[ insertChar[i]] = orig_pairs[i]
            else:
                charCount[ insertChar[i]] += orig_pairs[i]    
        orig_pairs = dest_pairs.copy()
        dest_pairs.clear()
    
    return max(charCount.values()) - min(charCount.values())

#Task 1

print( "Result Task 1: ", solve( 10))

#Task 2

print( "Result Task 2: ", solve( 40))


# AdventOfCode 2021
# Day 3

#get input data
sampleList = []
with open( "03.data", "r") as file:
    for line in file:
        sampleList.append( line.rstrip())
file.close()

#Task 1
ones = []
samples = len(sampleList)
numberOfBits = len(sampleList[0])
for i in range(0, numberOfBits):
    ones.append( 0)
for sample in sampleList:
    for bit in range(0,numberOfBits):
        if sample[bit] == "1":
            ones[bit] +=1

halveSizeOfList = samples / 2
gammaString = ""
epsilonString = ""
for count in ones:
    if count > halveSizeOfList:
        gammaString += "1"
        epsilonString += "0"
    else:
        gammaString += "0"
        epsilonString += "1"


gamma = int( gammaString, 2)
epsilon = int(epsilonString, 2)
print( "Result Task 1: gamma: ", gamma, "epsilon: ", epsilon, "solution: ", gamma * epsilon)

#Task 2

def getNewList( inputList, bitPosition, mostCommon):
    count = 0
    for testStr in inputList:
        if testStr[bitPosition] == "1":
            count += 1
    # mostCommon 1, count >= : targetBit 1
    #                     <  :           0
    #            0        >= :           0
    #                     <  :           1
    targetBit = str( mostCommon) if count >= len(inputList) / 2 else str( 1 - mostCommon)
    newList = []
    for testStr in inputList:
        if testStr[bitPosition] == targetBit:
            newList.append( testStr)
    if len(newList) == 1:
        return newList[0]
    return getNewList( newList, bitPosition + 1, mostCommon)

oxygen = int(getNewList( sampleList, 0, 1), 2)
co2 = int( getNewList( sampleList, 0, 0), 2)

print( "Result Task 2: Oxygen: ", oxygen, "CO2: ", co2, "solution: ", oxygen * co2)


# AdventOfCode 2021
# Day 3

#get input data
sampleList = []
with open( "03.data", "r") as file:
    for line in file:
        sampleList.append( line.rstrip())
file.close()

#sampleList = [ "0010", "0110", "0000", "1100"]

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
def getBitOneCount( bitList, pos, bitStr):
    count = 0
    for sample in bitList:
        if( sample[pos] == bitStr):
            count +=1
    return count

def getResultList( inputList, bitPosition, searchBit):
    resultList = []
    for str in inputList:
        if int(str[ bitPosition]) ==  searchBit:
            resultList.append( str)
    return resultList

#mostOrLeast: 1 = most common, 0 = least common
def getNumber( searchList, searchBit, mostOrLeast):
    sampleList = list( searchList)
    newList = []
    for bitPosition in range(0,len(sampleList[0])):
        count = getBitOneCount( sampleList, bitPosition, searchBit)
        commonBit = searchBit if count >= len(sampleList) / 2 else 1 - searchBit
        if not mostOrLeast:
            commonBit = 1 - commonBit
        sampleList = getResultList( sampleList, bitPosition, commonBit)    
        if len( sampleList) == 1:
            return sampleList[0]


oxygen = int(getNumber( sampleList, 1, 1), 2)
co2 = int( getNumber( sampleList, 1, 0), 2)


print( "Result Task 2: Oxygen: ", oxygen, "CO2: ", co2, "solution: ", oxygen * co2)


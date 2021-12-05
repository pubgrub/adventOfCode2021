# AdventOfCode 2021
# Day 4

#get input data
sampleList = []
with open( "04.data", "r") as file:
  for line in file:
    sampleList.append( line.rstrip())
file.close()

class BingoBoard:    
  
  def __init__(self, size, ints): # constructor method
    self.boardSize = size
    if len( ints) != self.boardSize**2:
      raise Exception( "Cannot create Board, wrong size. Expected: " + str(self.boardSize**2) + " got: " + str(len( ints)))
    self.numbers = ints[:]
    self.seen = [False] * len(self.numbers)


  def __str__(self):
    return( "Board: size -> " +  str(self.boardSize) +  
            "\nNumbers -> " + str( self.numbers) +
            "\nSeen -> " + str( self.seen))

# Task 1

b = BingoBoard( 3, [17,58,52,49,72,33,55,73,27])
print( b)
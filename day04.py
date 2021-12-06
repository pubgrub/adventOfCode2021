# AdventOfCode 2021
# Day 4

#get input data
from os import linesep


lines = []
with open( "04.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

draws = lines[0].split( ",")
del lines[0:2]
print( lines[0])

boards = []
board = []
for l in lines:
   if len(l) != 0:
     board.extend( int(i) for i in l.split())
   else:
     boards.append( board)
     board = []
if board != []:
  boards.append( board)


class BingoBoard:    
  
  def __init__(self, size, ints): # constructor method
    self.boardSize = size
    if len( ints) != self.boardSize**2:
      raise Exception( "Cannot create Board, wrong size. Expected: " + str(self.boardSize**2) + " got: " + str(len( ints)))
    self.numbers = ints[:]
    self.seen = [False] * len(self.numbers)
    self.rows = []
    for i in range(0,self.boardSize):
      self.rows.append([] )
      for j in range( 0, self.boardSize):
        self.rows[-1].append( i*self.boardSize + j)
    for i in range(0,self.boardSize):
      self.rows.append([] )
      for j in range( 0, self.boardSize):
        self.rows[-1].append( i + j * self.boardSize)

  def draw( self, num):
    if num in self.numbers:
      idx = self.numbers.index(num)
      self.seen[idx] = True

  def isSolved( self):
    for r in self.rows:
      try:
         [self.seen[x] for x in r].index(False)
      except:
        return True
    return False

  def getValue( self):
    idx = [i for i in range(0,len(self.numbers)) if self.seen[i] == False]
    v = 0
    for i in idx:
      v += self.numbers[i]
    return v

  def __str__(self):
    return( "Board: size -> " +  str(self.boardSize) +  
            "\nNumbers -> " + str( self.numbers) +
            "\nSeen -> " + str( self.seen))

# Task 1

b = BingoBoard( 3, [17,58,52,49,72,33,55,73,27])
print( b)
b.draw( 51)
b.draw( 52)
print( b)
print( b.isSolved())
b.draw( 17)
b.draw( 58)
print( b.isSolved())
print( b)
print( b.getValue())
# AdventOfCode 2021
# Day 4

#get input data
from os import linesep


lines = []
with open( "04.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

draws = [ int(x) for x in lines[0].split( ",")]
del lines[0:2]

boards = []
board = []
size = 0
for l in lines:
   if len(l) != 0:
     board.extend( int(i) for i in l.split())
   else:
     if size == 0:
       size = int( len(board)**0.5 )
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

bingoBoards = []
for b in boards:
  bingoBoards.append( BingoBoard( size, b))

def solve(): 
  for d in draws:
    for b in bingoBoards:
      b.draw(d)
      if b.isSolved():
        return( b.getValue() * d)
  return 0

result = solve()
print( "Result Task 1: ", result)

# Task 2

bingoBoards = []
for b in boards:
  bingoBoards.append( BingoBoard( size, b))

def solve(): 
  solved = [False] * len(bingoBoards)
  for d in draws:
    for b in bingoBoards:
      b.draw(d)
      if b.isSolved():
        solved[bingoBoards.index(b)] = True
        try:
          solved.index(False)
        except:
          return( b.getValue() * d)
  return 0

result = solve()
print( "Result Task 2: ", result)




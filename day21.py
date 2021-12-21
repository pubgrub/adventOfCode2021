# AdventOfCode 2021
# Day 21

#get input data

from operator import add

lines = []
with open( "21.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

playerPos = []
score=[]
for l in lines:
  dummy, pos = ( l.split( ': '))
  playerPos.append( int( pos))
  score.append(0)

startPos = playerPos.copy()
startScore = score.copy()

# Task 1

diceMin = 1
diceMax = 100

rolled = 0
firstRoll = 6
interval = 3
winScore = 1000
finished = False
while finished == False:
  for p in range( len( playerPos)):
    playerPos[ p] =  ( playerPos[ p] + firstRoll + interval * rolled) % 10  
    if playerPos[ p] == 0:
      playerPos[ p] = 10
    score[ p] += playerPos[ p]
    rolled += 3
    if score[ p] >= winScore:
      finished = True
      loser = 1 - p
      break

print( "Result Task 1: ", score[ loser] * rolled)

# Task 2

winGrid = {}

def roll( player, playerPos,  dice, numRoll, score):
  playerPos = playerPos.copy()
  score = score.copy()
  playerPos[ player] += dice 
  if playerPos[ player] > 10:
    playerPos[ player] -= 10
  
  tempScore = score[ player] + playerPos[ player]
  if numRoll == 3:
    if tempScore >= 21:
      wins = [ 0, 0]
      wins[ player] = 1
      return  wins
    score[ player] = tempScore
    numRoll = 0
    player = 1 - player
  numRoll += 1

  localWins = [ 0, 0]
  for d in range( 1, 4):
    if ( player, tuple( playerPos), tuple( score), d, numRoll) in winGrid:
      lastWins = winGrid[ ( player, tuple( playerPos), tuple( score), d, numRoll)]
    else:
      lastWins = roll( player, playerPos, d, numRoll, score)
      winGrid[ ( player, tuple( playerPos), tuple( score), d, numRoll)] = lastWins
    localWins[0] += lastWins[0]
    localWins[1] += lastWins[1]
  
  return localWins 

playerPos = startPos.copy()
score = startScore.copy()
wins = roll( 0, playerPos, 0, 0, score)

print( "Result Task 2: ", max( [ x for x in wins]))

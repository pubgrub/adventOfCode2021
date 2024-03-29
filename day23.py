# AdventOfCode 2021
# Day 23

#get input data
lines = []
with open( "23.data", "r") as file:
    for line in file:
        lines.append( line)
file.close()

destX = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
costPerStep = {'A': 1, 'B': 10, 'C': 100, 'D':1000} 

#bit numbering (index in coordBits (x,y))
#  8  9   10   11   12   13  14
#       4    5    6    7
#       0    1    2    3
coordBits = [ (2,2) ,(4,2), (6,2), (8,2),  
              (2,1), (4,1), (6,1), (8,1), 
              (0,0), (1,0), (3,0), (5,0),
              (7,0), (9,0), (10,0)]


possStops = 0b111111100000000
possDests = 0b000000011111111

def numberToBinaryString( n):
  return '{0:0b}'.format(n)

# Dec 10 -> Binary 1010 -> result 2, 8
def numberToBinaries( n):
  p = 1
  result = []
  for s in  list(numberToBinaryString(n))[::-1]:
    if s == '1':
      result.append( p)
    p *= 2
  return result

# Dec 10 -> Binary 1010 -> result 1, 3
def numberToBinaryPositions(n):
  p = 0
  result = []
  for s in  list(numberToBinaryString(n))[::-1]:
    if s == '1':
      result.append( p)
    p += 1
  return result

#bitfield of occupied spaces
occupied = 0

#list of players
players = []
playerInRow2 = []

for y,l in enumerate( lines[1:4]):
  for x,char in enumerate( list(l)[1:]):
    if char in "ABCD":
      pos = coordBits.index( (x,y))
      players.append( { 'name': char, 'pos': pos , 'completed': False, 'cost': costPerStep[ char]})
      occupied += 2 ** pos
      if y == 2:
        playerInRow2.append( char)
#this number indicates all players in room
allRoomsOccupied = occupied

#all possible routes from in to out and back
routes = {}

for start in numberToBinaryPositions( possDests):
  for end in numberToBinaryPositions(possStops):
    (sx, sy) = coordBits[start]
    (ex, ey) = coordBits[end]
    route = 0
    x = sx
    y = sy
    while y > ey:
      y -= 1
      if ( x, y) in coordBits:
        route += 2 ** coordBits.index(( x, y))
    while x > ex:
      x -= 1
      if ( x, y) in coordBits:
        route += 2 ** coordBits.index(( x, y))
    while x < ex:
      x += 1
      if ( x, y) in coordBits:
        route += 2 ** coordBits.index(( x, y))
    # possible routes in both directions
    routes[ (start, end)] = route
    route -= 2 ** end
    route += 2 ** start
    routes[ ( end, start)] = route


minSolveCost = -1

def solve( players, cost, player , toPos):
  if player >= 0:
    oldOccupied = occupied
    occupied -= 2 ** players[ player][ 'pos']
    occupied >= 2 ** toPos
    cost += players[player]['cost']
    if occupied == allRoomsOccupied:
      # solved
      if minSolveCost >= 0 and cost < minSolveCost:
        minSolveCost = cost
        occupied = oldOccupied
        return 
        
  for i, p in enumerate(players):
      name = p['name']    
      if 2 ** p['pos'] & possStops: 
        stops = possDests
      else:
        stops= possStops
      for dest in numberToBinaries( stops):



result = solve( players, 0, -1, -1)

print( possStops)
print( possDests)

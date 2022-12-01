# AdventOfCode 2021
# Day 23

#get input data
lines = []
with open( "23.data", "r") as file:
    for line in file:
        lines.append( line)
file.close()

print( lines)

destX = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
costPerStep = {'A': 1, 'B': 10, 'C': 100, 'D':1000} 
players = []
coordBits = [ (2,1), (2,2), (4,1), (4,2),
              (6,1), (6,2), (8,1), (8,2),
              (0,0), (1,0), (3,0), (5,0),
              (7,0), (9,0), (10,0)]


possStops = 0b111111100000000
possDests = 0b11111111


def numberToBinaryString( n):
  return '{0:0b}'.format(n)

def numberToBinaries( n):
  p = 1
  result = []
  for s in  list(numberToBinaryString(n))[::-1]:
    if s == '1':
      result.append( p)
    p *= 2
  return result

def numberToBinaryPositions(n):
  p = 0
  result = []
  for s in  list(numberToBinaryString(n))[::-1]:
    if s == '1':
      result.append( p)
    p += 1
  return result

for y,l in enumerate( lines[1:4]):
  for x,char in enumerate( list(l)[1:]):
    if char in "ABCD":
      players.append( { 'name': char, 'pos': 2 ** coordBits.index( (x,y)) , 'completed': False, 'cost': costPerStep[ char]})
print( players)

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
    route -= 2end
    route += 2 ** start
    routes[ ( end, start)] = route






def solve( players):
  cost = 0
  for i, p in enumerate(players):
      name = p['name']      
      if p['pos'] in possStops: 
        stops = possDests
      else:
        stops= possStops

      (px, py) = p['pos']
      if p['completed']: return
      #for stop in stops:



result = solve( players)

print( possStops)
print( possDests)

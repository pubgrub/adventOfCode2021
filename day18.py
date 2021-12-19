# AdventOfCode 2021
# Day 18

#get input data

lines = []
with open( "18.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

class Number:
  
  @staticmethod
  def buildTree( str, num):
    while str:
      if str[:1].isdigit(): # handle numbers > 9
        i = 1
        while( str[:i].isdigit()):
          i += 1
        s, str = str[ : i - 1], str[ i - 1:]
      else:
        s, str = str[ :1], str[ 1:]
      if s == '[':
        num = Number( num)
      elif s == ',' or s == ' ':
        continue
      elif s == ']':
        if num.parent != None:
          num = num.parent
      else:
        num.addChild( int(s))
    return num

  def __init__( self, parent):
    self.children = []
    self.parent = parent
    self.magnitude = 0
    if parent.__class__ == Number:
      parent.addChild( self)

  def getMagnitude(self):
    mag = 0
    mult = [ 3, 2]
    for i in range( len(self.children)):
      c = self.children[i]
      mag += mult[ i] * (c if c.__class__ == int else c.getMagnitude())
    return mag

  def getLeftChild( self):
    return self.children[0]

  def setLeftChild( self, child):
    self.children[0] = child

  def getRightChild( self):
    return self.children[1]

  def setRightChild( self, child):
    self.children[1] = child

  def addChild( self, child):
    self.children.append( child)

  def reduce( self):
    changed = True
    while changed:
      changed = False
      toExplode = self.searchForExplodingNumber()
      if toExplode:
        #print( "before ex: ", self.oneLineString(True), " -> ", toExplode.oneLineString())
        toExplode.explodeNumber()
        #print( "after  ex: ", self.oneLineString())
        #print( "after  ex: ", self.oneLineString(True))

        changed = True
        continue
      toSplit = self.searchForSplittingNumber()
      if toSplit:
        #print( "before sp: ", self.oneLineString(), " -> ", toSplit.oneLineString())
        toSplit.splitNumber()
        #print( "after  sp: ", self.oneLineString())
        changed = True


  def searchForExplodingNumber( self, lvl = 0):
    if lvl == 4:
      return self
    else:
      for c in self.children:
        if c.__class__ == Number:
          found = c.searchForExplodingNumber( lvl + 1)
          if found.__class__ == Number:
            return found
    return False  

  def explodeNumber( self):
    
    for i in range( len( self.children)):
      self.parent.addExplodeValue( i, 1, self.children[i], self)
    for i in range( len(self.parent.children)):
      if self.parent.children[i] == self:
        self.parent.children[i] = 0

  def addExplodeValue(  self, lr, upDown, value, sender):
      if upDown: #going up
        #print( "***", lr, upDown, value, self.children)
        if self.children[ lr].__class__  != Number:
          self.children[ lr] += value
          return
        elif self.children[ lr] == sender:  
          # coming up from the left
          if self.parent != None:
            self.parent.addExplodeValue( lr, upDown, value, self)
          else:
            return
        else:
          # changing direction, going down
          dir = lr
          lr = 1 - lr
          upDown = 0
          self.children[ dir].addExplodeValue( lr, upDown, value, self)
      else:
        if self.children[ lr].__class__ != Number:
          self.children[ lr] += value
          return
        else:
          self.children[lr].addExplodeValue( lr, upDown, value, self)


  def searchForSplittingNumber( self):
    found = False
    for i in self.children:
      if i.__class__ == int:
        #print( "found int")
        if i > 9:
          #print( "found >9")
          return self
      else:
        found = i.searchForSplittingNumber()
        if found:
          return found
    return found


  def splitNumber( self):
    for i in range( len(self.children)):
      child = self.children[ i]
      if child.__class__ == int and child > 9:
        newNumber = Number( None)
        self.children[i] = newNumber
        newNumber.parent = self
        child0 = int( child // 2)
        child1 = child - child0
        self.children[i].addChild( child0)
        self.children[i].addChild( child1)
        return

  def addNumber( self, num):
    newNumber = Number( None)
    newNumber.addChild( self)
    newNumber.addChild( num)
    self.parent = newNumber
    num.parent = newNumber
    return newNumber

  def __str__( self, level = 0):
    ret = "\t" * level + "Number:\n"
    for c in self.children:
      if c.__class__ == Number:
        ret += c.__str__( level + 1)
      else:
        ret += "\t" * level + c.__str__() + '\n'
    if level == 0:
      ret += self.oneLineString()
    return ret

  def oneLineString(self, colored = False):
    ret = '['
    for c in range( len(self.children)):
      ret += self.children[ c].oneLineString() if self.children[ c].__class__ == Number else str( self.children[ c])
      if c == 0:
        ret += ','
    ret += ']'

    if colored:
      # color coding
      lvl = 0
      color = {}
      colorString = [ "\033[1;31m", "\033[1;34m"]
      colorOffString = "\033[0;0m"
      for c in range( len( ret)):
        if ret[c] == ']':
          lvl -= 1
        if ret[c] == '[':
          lvl += 1
          if lvl >= 5:
            color[ c] = 0
        if ret[c].isdigit() and ret[c+1].isdigit():
          color[ c] = 1
          color[ c + 1] = 1

      for r in reversed(sorted( color)):
        ret = ret[:r] + colorString[ color[ r]] + ret[r] + colorOffString + ret[r+1:]
        #if color:
          #print( ret)

    return ret


#Task 1

l = lines[0]
tree = Number.buildTree( l, None)

for l in lines[ 1:]:
  addTree = Number.buildTree( l, None)
  #print( "both:  ", tree.oneLineString(), addTree.oneLineString())
  tree = tree.addNumber( addTree)
  #print( "added: ", tree.oneLineString())
  tree.reduce()
  #print( "redcd: ", tree.oneLineString())
#print( tree)
print( "Result Task 1: ", tree.getMagnitude())

#Task 2

maxMagnitude = 0
for i in lines:
  for j in lines:
    if j == i:
      continue
    num1 = Number.buildTree( i, None)
    num2 = Number.buildTree( j, None)
    num = num1.addNumber( num2)
    num.reduce()
    mag = num.getMagnitude()
    maxMagnitude = max( maxMagnitude, mag)
print( "Result Task 2: ", maxMagnitude)
# AdventOfCode 2021
# Day 18

#get input data

lines = []
with open( "18test.data", "r") as file:
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
    if parent.__class__ == Number:
      parent.addChild( self)

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
    {}

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
      if upDown:
        print( "***", lr, upDown, value, self.children)
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
          lr = 1 - lr
          upDown = 0
          dir = lr if self.children[ lr] != sender else 1 - lr
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
        print( "found int")
        if i > 9:
          print( "found >9")
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
    {}


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

  def oneLineString(self):
    ret = '['
    for c in range( len(self.children)):
      ret += self.children[ c].oneLineString() if self.children[ c].__class__ == Number else str( self.children[ c])
      if c == 0:
        ret += ','
    ret += ']'
    return ret



l = lines[0]
print( l)
tree = Number.buildTree( l, None)

print( tree)

# explode = tree.searchForExplodingNumber()
# print( "explode: \n", explode)
# if explode:
#   explode.explodeNumber()
toSplit = tree.searchForSplittingNumber()
print( "toSplit: ", toSplit)
toSplit.splitNumber()
print( tree)
# AdventOfCode 2021
# Day 16

#get input data

lines = []
with open( "16.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

bitStream = ''
bitStream = ''.join( [bin(int(x, 16))[2:].zfill(4) for x in list(lines[0]) ])

class Packet:

  SUM = 0
  PRODUCT = 1
  MINIMUM = 2
  MAXIMUM = 3
  LITERAL = 4
  GREATER_THAN = 5
  LESS_THAN = 6
  EQUAL_TO = 7

  version = 0
  type = ''
  
  def __new__( cls, bitStream):
    self = object.__new__( cls)

    # for literal type
    self.value = 0

    # for operator type
    self.subPackets = []

    self.version, bitStream = int( bitStream[ :3], 2), bitStream[ 3:]
    self.type, bitStream = int( bitStream[ :3], 2), bitStream[ 3:]

    if self.type == self.LITERAL:    
      notLastGroup = 1
      literalBits = ''
      while  notLastGroup:
        notLastGroup, bitStream = int( bitStream[ :1]), bitStream[ 1:]
        ( bits, bitStream) = bitStream[ :4], bitStream[ 4:]
        literalBits += bits
      self.value = int( literalBits, 2)
    else:
      (self.lengthTypeID, bitStream) = int( bitStream[ :1]), bitStream[ 1:]
      if self.lengthTypeID == 0:
        (subPacketsLength, bitStream) = int( bitStream[ :15], 2), bitStream[ 15:]
        (subPacketsBits, bitStream) = bitStream[ :subPacketsLength], bitStream[ subPacketsLength:]
        while subPacketsBits:
          (nextPacket, subPacketsBits) = Packet( subPacketsBits)
          self.subPackets.append( nextPacket)
      else:
        (self.numSubPackets, bitStream) = int(bitStream[ :11], 2), bitStream[ 11:]
        while self.numSubPackets > len(self.subPackets):
          (nextPacket, bitStream) = Packet( bitStream)
          self.subPackets.append( nextPacket)
    return (self, bitStream)

  def getSumOfVersions( self):
    if self.type == Packet.LITERAL:
      return self.version
    else:
      return self.version + sum(p.getSumOfVersions() for p in self.subPackets)

  def getValueOfOperatorPacket( self):
    if self.type == Packet.LITERAL:
      return self.value
    else:
      values = [p.getValueOfOperatorPacket() for p in self.subPackets]
      if self.type == self.SUM:
        return sum(values)
      elif self.type == self.PRODUCT:
        prod = 1
        for v in values:
          prod = prod * v
        return prod
      elif self.type == self.MINIMUM:
        return min( values)
      elif self.type == self.MAXIMUM:
        return max( values)
      elif self.type == self.GREATER_THAN:
        return 1 if values[0] > values[1] else 0 
      elif self.type == self.LESS_THAN:
        return 1 if values[0] < values[1] else 0 
      elif self.type == self.EQUAL_TO:
        return 1 if values[0] == values[1] else 0 

# fill classes from bitstream
(firstPacket, bitStream) = Packet( bitStream)

# Task 1
print( "Result Task 1: ", firstPacket.getSumOfVersions())

# Task 2
print( "Result Task 2: ", firstPacket.getValueOfOperatorPacket())




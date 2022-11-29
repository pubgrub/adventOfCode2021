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


# with open( "16bin.data", "w") as ofile:
#   ofile.write( bitstream)
# ofile.close()



class Packet:

  OPERATOR = 1
  LITERAL = 4

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



print( bitStream)
print( len(lines[0]), len(bitStream))

(firstPacket, bitStream) = Packet( bitStream)

print( firstPacket.getSumOfVersions())
exit(0)



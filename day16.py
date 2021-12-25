# AdventOfCode 2021
# Day 16

#get input data

lines = []
with open( "16test.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())
file.close()

bitStream = ''
bitStream = ''.join( [bin(int(x, 16))[2:].zfill(4) for x in list(lines[0]) ])

# with open( "16bin.data", "w") as ofile:
#   ofile.write( bitstream)
# ofile.close()

#print( bitstream)
#print( len(lines[0]), len(bitstream))

class Packet:

  def getBits( self, str, start, length):
    return str[ start: start + length]

  def getIntFromBits( self, str):
    return int( str, 2)

  def getIntBits( self, str, start, length):
    return self.getIntFromBits( self, self.getBits( self, str, start, length))

  @staticmethod
  def createFromBitStream( bitStream):
    version, bitStream = int( bitStream[ :3], 2), bitStream[ 3:]
    typeID, bitStream = int( bitStream[ :3], 2), bitStream[ 3:]
    if typeID == 4:
      packet = PacketLiteral( version, bitStream)
    else:
      packet = PacketOperator( version, bitStream)

    return packet

class PacketLiteral( Packet):
    
  def __init__( self, version, bitStream):
    self.version = version  
    notLastGroup = 1
    literalBits = ''
    
    while  notLastGroup:
      print( "b: ", bitStream)
      print( "***: ", bitStream[ :1])
      print("****")
      notLastGroup, bitStream = int( bitStream[ :1]), bitStream[ 1:]
      ( bits, bitStream) = bitStream[ :4], bitStream[ 4:]
      literalBits += bits
    self.value = int( literalBits, 2)
    self.remainingBitStream = bitStream

class PacketOperator( Packet):
  def __init__( self, version, bitStream):
    self.version = version
    self.subPackets = []
    (self.lengthTypeID, bitStream) = int( bitStream[ :1]), bitStream[ 1:]
    if self.lengthTypeID == 0:
      (subPacketsLength, bitStream) = int( bitStream[ :15], 2), bitStream[ 15:]
      (subPacketsBits, bitStream) = bitStream[ :subPacketsLength], bitStream[ subPacketsLength:]
      while bitStream:
        subPacket = self.createFromBitStream( subPacketsBits)
        self.subPackets.append( subPacket)
    elif self.lengthTypeID == 1:
      (numSubPackets, bitStream) = int(bitStream[ :11], 2), bitStream[ 11:]
      for n in range( numSubPackets):
        packet = self.createFromBitStream( bitStream)
        bitStream = packet.remainingBitStream
        self.subPackets.append( packet)



(packet, bitStream) = Packet.createFromBitStream( bitStream)

print( packet)
print( bitStream)

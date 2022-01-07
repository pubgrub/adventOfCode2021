# AdventOfCode 2021
# Day 24

#get input data

lines = []
with open( "24.data", "r") as file:
  for line in file:
    lines.append( line.rstrip())

program = []
for l in lines:
  program.append( tuple( l.split(' ')))
  if len( program[-1]) == 3 and program[-1][2].lstrip('-').isnumeric():
    program[-1] = (program[-1][0], program[-1][1], int( program[-1][2]))

#print( program)


serial = 100000000000000
found = False
serial = 39111111111111    
registers = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
serial_digits = [ int(x) for x in list( str(serial))]
for instr in program:
  if instr[0] == 'inp':
    registers[ instr[1]] = serial_digits.pop( 0) 
    print( registers[ 'w'], registers[ 'x'], registers[ 'y'], registers[ 'z'])
  elif instr[0] == 'add':
    if instr[2] in registers:
      registers[instr[1]] = registers[instr[1]] + registers[instr[2]]
    else:
      registers[instr[1]] = registers[instr[1]] + instr[2]
  elif instr[0] == 'mul':
    if instr[2] in registers:
      registers[instr[1]] = registers[instr[1]] * registers[instr[2]]
    else:
      registers[instr[1]] = registers[instr[1]] * instr[2]
  elif instr[0] == 'div':
    if instr[2] in registers:
      registers[instr[1]] = registers[instr[1]] // registers[instr[2]]
    else:
      registers[instr[1]] = registers[instr[1]] // instr[2]
  elif instr[0] == 'mod':
    if instr[2] in registers:
      registers[instr[1]] = registers[instr[1]] % registers[instr[2]]
    else:
      registers[instr[1]] = registers[instr[1]] % instr[2]
  elif instr[0] == 'eql':
    if instr[2] in registers:
      num2 = registers[instr[2]]
    else:
      num2 = instr[2]
    registers[instr[1]] = 1 if registers[instr[1]] == num2 else 0
if registers['z'] == 0:
  found = 1
else:
  print( serial, registers['z'])


div = [ 1, 1, 1, 26, 1, 26, 26,1, 26, 1, 1, 26, 26, 26]
add_x = [ 11, 11, 15, -14, 10, 0, -6, 13, -3, 13, 15, -2, -9, -2]
add_y = [ 6, 14, 13, 1, 6, 13, 6, 3, 8, 14, 4, 7, 15, 1]

for z in reversed( range(1000000)):
  z_orig = z
  for w in range( 1, 10):
    x = z_orig % 26
    z = z // div[ -1]
    x += add_x[ -1]
    if x == w:
      x = 0
    else: 
      x = 1
    z *= 25 * x + 1
    y = ( w + add_y[ -1]) * x
    z += y
    if z == 0:
      print( z_orig, z, w )

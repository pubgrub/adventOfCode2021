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
while not found:
  serial -= 1    
  registers = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
  serial_digits = [ int(x) for x in list( str(serial))]
  if 0 in serial_digits:
    continue
  for instr in program:
    if instr[0] == 'inp':
      registers[ instr[1]] = serial_digits.pop() 
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

print( serial)
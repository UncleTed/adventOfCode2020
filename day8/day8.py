accumulator = 0
instruction_pointer = 0
program = []
with open("./input.txt", "r") as f:
    for line in f:
        code = line.rstrip().split(' ')
        instruction = {}
        instruction['op_code'] = code[0]
        instruction['value'] = int(code[1])
        instruction['has_already_been_executed'] = False
        program.append(instruction)

while instruction_pointer < len(program):
    c = program[instruction_pointer]
    print (f"ip: {instruction_pointer} op: {c['op_code']} {c['value']}")

    if c['has_already_been_executed']:
        print(f'Previously executed instruction exception! instruction pointer {instruction_pointer} accumulator {accumulator}')
        break
    if c['op_code'] == 'nop':
        instruction_pointer = instruction_pointer + 1
        c['has_already_been_executed'] = True
        continue
    if c['op_code'] == 'acc':
        accumulator = accumulator + c['value']
        instruction_pointer = instruction_pointer + 1
        c['has_already_been_executed'] = True
        continue
    if c['op_code'] == 'jmp':
        instruction_pointer = instruction_pointer + c['value']
        c['has_already_been_executed'] = True
        continue

print(f'Program finished. instruction pointer {instruction_pointer} accumulator {accumulator}')

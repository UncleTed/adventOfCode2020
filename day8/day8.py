import copy

program = []


class PreviouslyExecutedInstructionException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def execute_program(p):
    instruction_pointer = 0
    accumulator = 0
    while instruction_pointer < len(p):
        c = p[instruction_pointer]
        # print (f"ip: {instruction_pointer} op: {c['op_code']} {c['value']}")

        if c['has_already_been_executed']:
            raise PreviouslyExecutedInstructionException(f"instruction pointer {instruction_pointer} accumulator {accumulator}")
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
        
    return (instruction_pointer, accumulator)


with open("./input.txt", "r") as f:
    for line in f:
        code = line.rstrip().split(' ')
        instruction = {}
        instruction['op_code'] = code[0]
        instruction['value'] = int(code[1])
        instruction['has_already_been_executed'] = False
        program.append(instruction)

    iterations = 0   
    
    while True:
        # make copy of program
        p1 = copy.deepcopy(program)
        iterations = iterations + 1
        number_of_changes = 0
        i = 0
        while i < len(p1):
            if p1[i]['op_code'] == 'nop':
                number_of_changes = number_of_changes + 1
                if number_of_changes == iterations:
                    p1[i]['op_code'] = 'jmp'
                    # print('nop')
                    break
            if p1[i]['op_code'] == 'jmp':
                number_of_changes = number_of_changes + 1
                if number_of_changes == iterations:
                    p1[i]['op_code'] = 'nop'
                    # print('jmp')
                    break
            i = i + 1
        try:
            print(iterations)
            success = execute_program(p1)
            print(success)
            break
        except PreviouslyExecutedInstructionException:
            pass
        
        # change op_code if this is the nth try
        # try:
        # execute_program(p1)
        # break
        # except PreviouslyExecutedInstructionException:
        # iterations = iterations + 1
        #     
    # print([n for i, n in enumerate(program) if n['op_code'] == 'nop' or n['op_code'] == 'jmp'][1])
    
    # execute_program(program)
    



# print(f'Program finished. instruction pointer {instruction_pointer} accumulator {accumulator}')

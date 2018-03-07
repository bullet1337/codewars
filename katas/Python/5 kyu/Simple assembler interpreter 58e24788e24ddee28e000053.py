# https://www.codewars.com/kata/58e24788e24ddee28e000053
def simple_assembler(program):
    ip = 0
    registers = {}
    while ip < len(program):
        instruction, *operands = program[ip].split()
        if instruction == 'mov':
            registers[operands[0]] = registers[operands[1]] if operands[1].isalpha() else int(operands[1])
        elif instruction == 'inc':
            registers[operands[0]] += 1
        elif instruction == 'dec':
            registers[operands[0]] -= 1
        elif instruction == 'jnz':
            if (registers[operands[0]] if operands[0].isalpha() else int(operands[0])) != 0:
                ip += int(operands[1])
                continue
        ip += 1

    return registers
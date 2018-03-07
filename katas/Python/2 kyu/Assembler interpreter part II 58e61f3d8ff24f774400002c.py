# https://www.codewars.com/kata/58e61f3d8ff24f774400002c
class Frame:
    def __init__(self, ip=0):
        self.ip = ip
        self.cmp = 0


def mov(operands, frame):
    registers[operands[0]] = registers[operands[1]] if operands[1].isalpha() else int(operands[1])
    frame.ip += 1


def inc(operands, frame):
    registers[operands[0]] += 1
    frame.ip += 1


def dec(operands, frame):
    registers[operands[0]] -= 1
    frame.ip += 1


def add(operands, frame):
    registers[operands[0]] += registers[operands[1]] if operands[1].isalpha() else int(operands[1])
    frame.ip += 1


def sub(operands, frame):
    registers[operands[0]] -= registers[operands[1]] if operands[1].isalpha() else int(operands[1])
    frame.ip += 1


def mul(operands, frame):
    registers[operands[0]] *= registers[operands[1]] if operands[1].isalpha() else int(operands[1])
    frame.ip += 1


def div(operands, frame):
    registers[operands[0]] //= registers[operands[1]] if operands[1].isalpha() else int(operands[1])
    frame.ip += 1


def jmp(operands, frame):
    frame.ip = labels_map[operands[0]]


def call(operands, frame):
    frames.append(Frame(labels_map[operands[0]]))
    frame.ip += 1


def ret(operands, frame):
    frames.pop()


def end(operands, frame):
    global success
    success = True
    frames.pop()


def msg(operands, frame):
    global output
    output = ''.join(operand[1:-1] if operand[0] == "'" else str(registers[operand]) for operand in operands)
    frame.ip += 1


def cmp(operands, frame):
    frame.cmp = (registers[operands[0]] if operands[0].isalpha() else int(operands[0])) \
                - (registers[operands[1]] if operands[1].isalpha() else int(operands[1]))
    frame.ip += 1


def jne(operands, frame):
    if frame.cmp != 0:
        frame.ip = labels_map[operands[0]]
    else:
        frame.ip += 1


def je(operands, frame):
    if frame.cmp == 0:
        frame.ip = labels_map[operands[0]]
    else:
        frame.ip += 1


def jge(operands, frame):
    if frame.cmp >= 0:
        frame.ip = labels_map[operands[0]]
    else:
        frame.ip += 1


def jg(operands, frame):
    if frame.cmp > 0:
        frame.ip = labels_map[operands[0]]
    else:
        frame.ip += 1


def jle(operands, frame):
    if frame.cmp <= 0:
        frame.ip = labels_map[operands[0]]
    else:
        frame.ip += 1


def jl(operands, frame):
    if frame.cmp < 0:
        frame.ip = labels_map[operands[0]]
    else:
        frame.ip += 1


def parse(program):
    instructions = []
    instruction = []
    token = ''
    i = 0
    end = False
    while i < len(program):
        c = program[i]
        if c == "'":
            token += c
            i += 1
            while i < len(program) and program[i] != "'":
                token += program[i]
                i += 1
            token += program[i]
        elif c == ';':
            if instruction:
                instructions.append(instruction)
                instruction = []
            i += 1
            while i < len(program) and program[i] != '\n':
                i += 1
        elif c == ':':
            labels_map[token] = len(instructions)
            token = ''
        elif c == '\n':
            if token:
                instruction.append(token)
                end |= token == 'end'
                token = ''
                instructions.append(instruction)
                instruction = []
        elif c == ' ' or c == ',' or c == '\t':
            if token:
                end |= token == 'end'
                instruction.append(token)
                token = ''
        else:
            token += c

        i += 1
    if token:
        end |= token == 'end'
        instruction.append(token)
        instructions.append(instruction)

    return instructions if end else None


def assembler_interpreter(program):
    global registers, labels_map, frames, success, output
    registers = {}
    labels_map = {}
    frames = [Frame()]
    success = False
    output = None


    instructions_map = {
        'mov': mov, 'inc': inc, 'dec': dec, 'add': add, 'sub': sub, 'mul': mul, 'div': div, 'jmp': jmp, 'cmp': cmp,
        'jne': jne, 'je': je, 'jge': jge, 'jg': jg, 'jle': jle, 'jl': jl, 'call': call, 'ret': ret, 'msg': msg,
        'end': end
    }

    instructions = parse(program)
    if instructions is None:
        return -1

    while frames and frames[-1].ip < len(instructions):
        instruction, *operands = instructions[frames[-1].ip]
        instructions_map[instruction](operands, frame=frames[-1])

    return output if success else -1
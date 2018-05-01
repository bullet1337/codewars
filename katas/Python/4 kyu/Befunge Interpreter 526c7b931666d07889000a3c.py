# https://www.codewars.com/kata/526c7b931666d07889000a3c
from operator import add, sub, mul, truediv, mod
from random import randint

simple_operators = {'+': add, '-': sub, '*': mul, '/': truediv, '%': mod}
moves = {'>': [0, 1], '<': [0, -1], '^': [-1, 0], 'v': [1, 0]}
condition_moves = {'_': '<>', '|': '^v'}


def interpret(code):
    code = [list(line) for line in code.split('\n')]
    output = ''
    i = j = 0
    stack = []
    ascii = False
    skip = False
    move = moves['>']
    while code[i][j] != '@':
        instruction = code[i][j]
        if instruction == '"':
            ascii = not ascii
        elif instruction.isdigit() or ascii:
            stack.append(ord(instruction) if ascii else int(instruction))
        elif instruction in simple_operators:
            a, b = stack.pop(), stack.pop()
            if instruction in '/%' and a == 0:
                stack.append(0)
            else:
                stack.append(simple_operators[instruction](b, a))
        elif instruction == '!':
            stack.append(int(stack.pop() == 0))
        elif instruction == '`':
            stack.append(int(stack.pop() < stack.pop()))
        elif instruction in moves:
            move = moves[instruction]
        elif instruction == '?':
            move = moves['><^v'[randint(0, 3)]]
        elif instruction in condition_moves:
            move = moves[condition_moves[instruction][stack.pop() == 0]]
        elif instruction == ':':
            stack.append(stack[-1] if stack else 0)
        elif instruction == '\\':
            if len(stack) == 1:
                stack.append(0)
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(a)
                stack.append(b)
        elif instruction == '$':
            stack.pop()
        elif instruction == '.':
            output += str(stack.pop())
        elif instruction == ',':
            output += chr(stack.pop())
        elif instruction == '#':
            skip = True
        elif instruction == 'p':
            x, y, v = stack.pop(), stack.pop(), stack.pop()
            code[x][y] = chr(v)
        elif instruction == 'g':
            x, y = stack.pop(), stack.pop()
            stack.append(ord(code[x][y]))

        i = (i + move[0] + int(skip and move[0])) % len(code)
        j = (j + move[1] + int(skip and move[1])) % len(code[i])
        skip = False
    return output
    
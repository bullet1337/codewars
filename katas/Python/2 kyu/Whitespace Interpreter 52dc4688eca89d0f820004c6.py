# https://www.codewars.com/kata/52dc4688eca89d0f820004c6
import re
from collections import defaultdict


def parse_int(code, i):
    i += 1
    if code[i] == '\n':
        raise SyntaxError
    sign = 1 if code[i] == ' ' else -1
    i += 1
    bin = '0'
    while code[i] != '\n':
        bin += '0' if code[i] == ' ' else '1'
        i += 1
    return i, int(bin, 2) * sign


def parse_label(code, i):
    label = ''
    i += 1
    while code[i] != '\n':
        label += code[i]
        i += 1
    return i, label


def bind(f, *args):
    return lambda: f(*args)


def read_int(input):
    number = ''
    while input and input[0] != '\n':
        number += input.pop(0)
    if not input:
        raise RuntimeError

    input.pop(0)
    return int(number)


output = ip = clean = input = stack = calls = heap = labels = commands = None


def whitespace(code, inp=''):
    global output, ip, clean, input, stack, calls, labels, commands
    output = ''
    ip = 0
    clean = False
    input = list(inp)
    code = re.sub('[^ \t\n]', '', code)
    stack = []
    calls = []
    heap = defaultdict(int)
    labels = {}
    commands = []

    def discard(n):
        global stack
        if 0 <= n < len(stack):
            stack = stack[:-1 - n] + stack[-1:]
        else:
            stack = stack[-1:]

    def dup(n):
        if n < 0:
            raise RuntimeError
        stack.append(stack[-1 - n])

    def swap():
        stack[-2:] = stack[:-3:-1]

    def div():
        a, b = stack.pop(), stack.pop()
        stack.append(b // a)

    def mod():
        a, b = stack.pop(), stack.pop()
        stack.append(b % a)

    def heap_put():
        a, b = stack.pop(), stack.pop()
        heap[b] = a

    def heap_get():
        a = stack.pop()
        if a not in heap:
            raise RuntimeError
        stack.append(heap[a])

    def out_char():
        global output
        output += chr(stack.pop())

    def out_num():
        global output
        output += str(stack.pop())

    def in_char():
        heap[stack.pop()] = ord(input.pop(0))

    def in_num():
        heap[stack.pop()] = read_int(input)

    def call(label):
        global ip
        calls.append(ip + 1)
        ip = labels[label] - 1

    def ret():
        global ip
        ip = calls.pop() - 1

    def exit():
        global ip, clean
        ip = len(commands) - 1
        clean = True

    def jump(label, condition=None):
        global ip
        if condition is None:
            ip = labels[label] - 1
        else:
            n = stack.pop()
            if condition and n == 0 or not condition and n < 0:
                ip = labels[label] - 1

    i = j = 0
    while i < len(code):
        if code[i] == ' ':
            i += 1
            if code[i] == ' ':
                i, n = parse_int(code, i)
                commands.append(bind(stack.append, n))
            elif code[i] == '\t':
                i += 1
                if code[i] == ' ':
                    i, n = parse_int(code, i)
                    commands.append(bind(dup, n))
                elif code[i] == '\n':
                    i, n = parse_int(code, i)
                    commands.append(bind(discard, n))
            elif code[i] == '\n':
                i += 1
                if code[i] == ' ':
                    commands.append(lambda: stack.append(stack[-1]))
                elif code[i] == '\t':
                    commands.append(swap)
                elif code[i] == '\n':
                    commands.append(lambda: stack.pop())
        elif code[i] == '\t':
            i += 1
            if code[i] == ' ':
                i += 1
                if code[i] == ' ':
                    i += 1
                    if code[i] == ' ':
                        commands.append(lambda: stack.append(stack.pop() + stack.pop()))
                    elif code[i] == '\t':
                        commands.append(lambda: stack.append(-(stack.pop() - stack.pop())))
                    elif code[i] == '\n':
                        commands.append(lambda: stack.append(stack.pop() * stack.pop()))
                    else:
                        raise SyntaxError
                elif code[i] == '\t':
                    i += 1
                    if code[i] == ' ':
                        commands.append(div)
                    elif code[i] == '\t':
                        commands.append(mod)
                    else:
                        raise SyntaxError
                else:
                    raise SyntaxError
            elif code[i] == '\t':
                i += 1
                if code[i] == ' ':
                    commands.append(heap_put)
                elif code[i] == '\t':
                    commands.append(heap_get)
                else:
                    raise SyntaxError
            elif code[i] == '\n':
                i += 1
                if code[i] == ' ':
                    i += 1
                    if code[i] == ' ':
                        commands.append(out_char)
                    elif code[i] == '\t':
                        commands.append(out_num)
                    else:
                        raise SyntaxError
                elif code[i] == '\t':
                    i += 1
                    if code[i] == ' ':
                        commands.append(in_char)
                    elif code[i] == '\t':
                        commands.append(in_num)
                    else:
                        raise SyntaxError
                else:
                    raise SyntaxError
            else:
                raise SyntaxError
        elif code[i] == '\n':
            i += 1
            if code[i] == ' ':
                i += 1
                if code[i] == ' ':
                    i, l = parse_label(code, i)
                    if l in labels:
                        raise SyntaxError
                    labels[l] = len(commands)
                elif code[i] == '\t':
                    i, l = parse_label(code, i)
                    commands.append(bind(call, l))
                elif code[i] == '\n':
                    i, l = parse_label(code, i)
                    commands.append(bind(jump, l))
                else:
                    raise SyntaxError
            elif code[i] == '\t':
                i += 1
                if code[i] == ' ':
                    i, l = parse_label(code, i)
                    commands.append(bind(jump, l, True))
                elif code[i] == '\t':
                    i, l = parse_label(code, i)
                    commands.append(bind(jump, l, False))
                elif code[i] == '\n':
                    commands.append(ret)
                else:
                    raise SyntaxError
            elif code[i] == '\n':
                i += 1
                if code[i] == '\n':
                    commands.append(exit)
                else:
                    raise SyntaxError
            else:
                raise SyntaxError
        else:
            raise SyntaxError
        i += 1
        j = i

    while ip < len(commands):
        commands[ip]()
        ip += 1
    if not clean:
        raise RuntimeError
    return output

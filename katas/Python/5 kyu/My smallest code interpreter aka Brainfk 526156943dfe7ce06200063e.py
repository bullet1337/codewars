# https://www.codewars.com/kata/526156943dfe7ce06200063e
from collections import defaultdict


def brain_luck(code, input):
    input = iter(input)
    data = defaultdict(int)
    brackets = []
    ip = dp =    0
    output = ''
    while ip < len(code):
        instruction = code[ip]
        if instruction == '>':
            dp += 1
        elif instruction == '<':
            dp -= 1
        elif instruction == '+':
            data[dp] = (data[dp] + 1) & 255
        elif instruction == '-':
            data[dp] = (data[dp] - 1) & 255
        elif instruction == '.':
            output += chr(data[dp])
        elif instruction == ',':
            data[dp] = ord(next(input))
        elif instruction == '[':
            if data[dp] == 0:
                brc = 1
                while ip < len(code) - 1 and brc != 0:
                    ip += 1
                    if code[ip] == '[':
                        brc += 1
                    elif code[ip] == ']':
                        brc -= 1
            else:
                brackets.append(ip)
        elif instruction == ']':
            if data[dp] != 0:
                ip = brackets[-1]
            else:
                brackets.pop()
        ip += 1
    return output
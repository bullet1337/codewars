# https://www.codewars.com/kata/59a9735a485a4d807f00008a
from collections import defaultdict


def poohbear(code):
    data = defaultdict(int)
    brackets = []
    ip = dp = 0
    output = ''
    copy = 0
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
        elif instruction == 'T':
            data[dp] = (data[dp] << 1) & 255
        elif instruction == 'Q':
            data[dp] = (data[dp] ** 2) & 255
        elif instruction == 'U':
            data[dp] = int(data[dp] ** .5) & 255
        elif instruction == 'L':
            data[dp] = (data[dp] + 2) & 255
        elif instruction == 'I':
            data[dp] = (data[dp] - 2) & 255
        elif instruction == 'V':
            data[dp] = (data[dp] >> 1) & 255
        elif instruction == 'A':
            data[dp] = (data[dp] + copy) & 255
        elif instruction == 'B':
            data[dp] = (data[dp] - copy) & 255
        elif instruction == 'Y':
            data[dp] = (data[dp] * copy) & 255
        elif instruction == 'D':
            data[dp] = int(data[dp] / copy) & 255
        elif instruction == 'c':
            copy = data[dp]
        elif instruction == 'p':
            data[dp] = copy
        elif instruction == 'P':
            output += chr(data[dp])
        elif instruction == 'N':
            output += str(data[dp])
        elif instruction == 'W':
            if data[dp] == 0:
                brc = 1
                while ip < len(code) - 1 and brc != 0:
                    ip += 1
                    if code[ip] == 'W':
                        brc += 1
                    elif code[ip] == 'E':
                        brc -= 1
            else:
                brackets.append(ip)
        elif instruction == 'E':
            if data[dp] != 0:
                ip = brackets[-1]
            else:
                brackets.pop()
        ip += 1
    return output

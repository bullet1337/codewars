# https://www.codewars.com/kata/5861487fdb20cff3ab000030
from collections import defaultdict


def to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:].zfill(8)
        result.extend(int(b) for b in bits[::-1])
    return result


def from_bits(bits):
    return ''.join(chr(int(''.join(str(bit) for bit in bits[i:i + 8][::-1]), 2)) for i in range(0, len(bits), 8))


def boolfuck(code, input=''):
    input = to_bits(input)
    data = defaultdict(bool)
    brackets = []
    ip = dp = in_p = 0
    output = []
    while ip < len(code):
        instruction = code[ip]
        if instruction == '>':
            dp += 1
        elif instruction == '<':
            dp -= 1
        elif instruction == '+':
            data[dp] = not data[dp]
        elif instruction == ';':
            output.append(int(data[dp]))
        elif instruction == ',':
            if in_p < len(input):
                data[dp] = input[in_p]
                in_p += 1
            else:
                data[dp] = 0
        elif instruction == '[':
            if data[dp]:
                brackets.append(ip)
            else:
                brc = 1
                while ip < len(code) - 1 and brc != 0:
                    ip += 1
                    if code[ip] == '[':
                        brc += 1
                    elif code[ip] == ']':
                        brc -= 1
        elif instruction == ']':
            if data[dp]:
                ip = brackets[-1]
            else:
                brackets.pop()
        ip += 1
    return from_bits(output)
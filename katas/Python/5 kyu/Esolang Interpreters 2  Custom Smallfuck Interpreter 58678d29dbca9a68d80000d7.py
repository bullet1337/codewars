# https://www.codewars.com/kata/58678d29dbca9a68d80000d7
def interpreter(code, data):
    data = list(data)
    brackets = []
    ip = dp = 0
    while ip < len(code) and 0 <= dp < len(data):
        instruction = code[ip]
        if instruction == '>':
            dp += 1
        elif instruction == '<':
            dp -= 1
        elif instruction == '*':
            data[dp] = '1' if data[dp] == '0' else '0'
        elif instruction == '[':
            if data[dp] == '0':
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
            if data[dp] != '0':
                ip = brackets[-1]
            else:
                brackets.pop()
        ip += 1
    return ''.join(data)

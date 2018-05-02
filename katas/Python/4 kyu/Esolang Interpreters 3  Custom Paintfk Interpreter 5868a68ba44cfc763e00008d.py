# https://www.codewars.com/kata/5868a68ba44cfc763e00008d
def interpreter(code, iterations, width, height):
    data = [['0' for _ in range(width)] for _ in range(height)]
    brackets = []
    ip = x = y = 0
    while ip < len(code) and iterations:
        instruction = code[ip]
        if instruction == 'n':
            x = (x - 1) % height
            iterations -= 1
        elif instruction == 's':
            x = (x + 1) % height
            iterations -= 1
        if instruction == 'e':
            y = (y + 1) % width
            iterations -= 1
        elif instruction == 'w':
            y = (y - 1) % width
            iterations -= 1
        elif instruction == '*':
            data[x][y] = '1' if data[x][y] == '0' else '0'
            iterations -= 1
        elif instruction == '[':
            if data[x][y] == '0':
                brc = 1
                while ip < len(code) - 1 and brc != 0:
                    ip += 1
                    if code[ip] == '[':
                        brc += 1
                    elif code[ip] == ']':
                        brc -= 1
            else:
                brackets.append(ip)
            iterations -= 1
        elif instruction == ']':
            if data[x][y] != '0':
                ip = brackets[-1]
            else:
                brackets.pop()
            iterations -= 1
        ip += 1
    return '\r\n'.join(''.join(row) for row in data)
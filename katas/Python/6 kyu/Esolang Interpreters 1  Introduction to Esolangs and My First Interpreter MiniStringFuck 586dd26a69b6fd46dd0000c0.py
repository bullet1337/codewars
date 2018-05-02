# https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0
def my_first_interpreter(code):
    data = 0
    output = ''
    for instruction in code:
        if instruction == '+':
            data = (data + 1) & 255
        elif instruction == '.':
            output += chr(data)
    return output

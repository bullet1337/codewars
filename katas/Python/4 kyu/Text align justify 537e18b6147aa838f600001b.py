# https://www.codewars.com/kata/537e18b6147aa838f600001b
def add_line(text, line, width, length):
    if len(line) == 1:
        text += line[0]
    else:
        div, mod = divmod(width - length + len(line), len(line) - 1)
        for i in range(len(line) - 1):
            text += line[i] + ' ' * (div + int(i < mod))
        text += line[-1]
    return text


def justify(text, width):
    tokens = text.split()
    line = []
    length = 0
    justified = ''
    for token in tokens:
        if length + len(token) <= width:
            line.append(token)
            length += len(token) + 1
        else:
            justified = add_line(justified, line, width, length)

            justified += '\n'
            line = [token]
            length = len(token) + 1
    justified += ' '.join(line)

    return justified
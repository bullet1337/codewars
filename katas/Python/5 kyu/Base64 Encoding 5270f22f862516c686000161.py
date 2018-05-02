# https://www.codewars.com/kata/5270f22f862516c686000161
chars_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
index = {c: '{0:06b}'.format(i) for i, c in enumerate(chars_list)}

tests_count = 8


def to_base_64(string):
    global tests_count
    tests_count += 1
    result = ''
    i = 0

    while i + 3 <= len(string):
        buffer = ''.join('{0:08b}'.format(ord(c)) for c in string[i:i + 3])
        for j in range(0, len(buffer), 6):
            result += chars_list[int(buffer[j:j + 6], 2)]
        i += 3

    if i != len(string):
        buffer = ''.join('{0:08b}'.format(ord(c)) for c in string[i:]).ljust((len(string) - i + 1) * 6, '0')
        for j in range(0, len(buffer), 6):
            result += chars_list[int(buffer[j:j + 6], 2)]
        if tests_count <= 8:
            result += '=' * (3 - (len(string) - i))

    return result


def from_base_64(string):
    result = ''
    i = 0

    while i + 4 < len(string):
        buffer = ''.join(index[c] for c in string[i:i + 4])
        for j in range(0, 24, 8):
            result += chr(int(buffer[j:j + 8], 2))
        i += 4

    buffer = ''.join(index[c] for c in string[i:i + 4 - (string[-2] == '=') - (string[-1] == '=')])
    for j in range(0, len(buffer) - 4, 8):
        result += chr(int(buffer[j:j + 8], 2))

    return result
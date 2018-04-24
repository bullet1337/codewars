# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
def spiralize(size):
    index = 0
    m = [[0 for _ in range(size)] for _ in range(size)]
    while index < size / 2:
        for i in range(index, size - index):
            m[index][i] = 1
            m[i][size - index - 1] = 1
            if size - index - 1 - index > 1:
                m[size - index - 1][i] = 1
                m[i][index] = 1

        if index + 1 < size:
            m[index + 1][index] = 0
        if size - index - 1 - index - 1 > 2:
            m[index + 2][index + 1] = 1

        index += 2

    return m
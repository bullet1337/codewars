# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
from itertools import chain



def snail(array):
    if len(array) != len(array[0]):
        return []

    return [x for k in range(len(array) // 2 + len(array) % 2) for x in
        chain(
            (array[k][i] for i in range(k, len(array) - k)),
            (array[i][len(array) - 1 - k] for i in range(1 + k, len(array) - 1 - k)),
            (array[len(array) - 1 - k][i] for i in range(len(array) - 1 - k, -1 + k, -1))
                if len(array) - 1 - k != k else (),
            (array[i][k] for i in range(len(array) - 2 - k, k, -1))
        )
    ]
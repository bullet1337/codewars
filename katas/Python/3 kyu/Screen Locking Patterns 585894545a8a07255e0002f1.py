# https://www.codewars.com/kata/585894545a8a07255e0002f1
blocks = {
    'A': {'B': 'C', 'E': 'I', 'D': 'G'},
    'B': {'E': 'H'},
    'C': {'B': 'A', 'E': 'G', 'F': 'I'},
    'D': {'E': 'F'},
    'E': {},
    'F': {'E': 'D'},
    'G': {'D': 'A', 'E': 'C', 'H': 'I'},
    'H': {'E': 'B'},
    'I': {'E': 'A', 'F': 'C', 'H': 'G'}
}

neighbors = {
    'A': {'B', 'D', 'E', 'F', 'H'},
    'B': {'A', 'C', 'D', 'E', 'F', 'G', 'I'},
    'C': {'B', 'D', 'E', 'F', 'H'},
    'D': {'A', 'B', 'C', 'E', 'G', 'H', 'I'},
    'E': {'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'},
    'F': {'A', 'B', 'C', 'E', 'G', 'H', 'I'},
    'G': {'B', 'D', 'E', 'F', 'H'},
    'H': {'A', 'C', 'D', 'E', 'F', 'G', 'I'},
    'I': {'B', 'D', 'E', 'F', 'H'}
}


def count_patterns_from(last, length, history=set()):
    if length == 1:
        return 1
    elif not(0 < length <= 9):
        return 0

    result = 0
    for point in neighbors[last].difference(history):
        history.add(last)
        result += count_patterns_from(point, length - 1, history)
        history.remove(last)

    for point in (v for k, v in blocks[last].items() if k in history and v not in history):
        history.add(last)
        result += count_patterns_from(point, length - 1, history)   
        history.remove(last)

    return result

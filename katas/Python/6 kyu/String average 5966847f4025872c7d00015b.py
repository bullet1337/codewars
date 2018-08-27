# https://www.codewars.com/kata/5966847f4025872c7d00015b
w2n = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

n2w = {v: k for k, v in w2n.items()}


def average_string(s):
    if not s:
        return 'n/a'

    try:
        return n2w[sum(w2n.get(number) for number in s.split()) // (s.count(' ') + 1)]
    except TypeError:
        return 'n/a'
# https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d
from collections import Counter


def build_code_table(freqs):
    tree = {}
    freqs = sorted(freqs, key=lambda x: x[::-1], reverse=True)
    while len(freqs) > 1:
        min1, min2 = freqs.pop(), freqs.pop()
        node = (min1[0] + min2[0], min1[1] + min2[1])
        tree[node[0]] = [min2[0], min1[0]]
        for i in range(len(freqs)):
            if freqs[i][1] < node[1]:
                freqs.insert(i, node)
                break
        else:
            freqs.append(node)

    table = {}
    stack = [(node[0], '')]
    while stack:
        n = stack.pop()
        if n[0] in tree:
            for i, child in enumerate(tree[n[0]]):
                stack.append((child, n[-1] + str(i)))
        else:
            table[n[0]] = n[1]
    return table


def frequencies(s):
    return list(Counter(s).items())


def encode(freqs, s):
    if len(freqs) < 2:
        return None
    elif not s:
        return ''

    table = build_code_table(freqs)
    return ''.join(table[c] for c in s)


def decode(freqs, bits):
    if len(freqs) < 2:
        return None
    elif not bits:
        return ''

    inverse_table = {v: k for k, v in build_code_table(freqs).items()}
    code = result = ''
    for bit in bits:
        code += bit
        if code in inverse_table:
            result += inverse_table[code]
            code = ''
    return result
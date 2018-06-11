# https://www.codewars.com/kata/59a818191c55c44f3900053f
def true_binary(n):
    return [1 if c == '1' else -1 for c in '1' + bin(n)[2:-1]]
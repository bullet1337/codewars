# https://www.codewars.com/kata/5596f6e9529e9ab6fb000014
def shifted_diff(first, second):
    for i in range(len(first)):
        if first[:len(first) - i] == second[i:] and first[len(second) - i:] == second[:i]:
            return i
    return -1
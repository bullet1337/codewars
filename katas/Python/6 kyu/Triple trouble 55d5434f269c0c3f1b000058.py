# https://www.codewars.com/kata/55d5434f269c0c3f1b000058
def triple_double(num1, num2):
    return any(chr(c) * 3 in str(num1) and chr(c) * 2 in str(num2) for c in range(ord('0'), ord('9') + 1))
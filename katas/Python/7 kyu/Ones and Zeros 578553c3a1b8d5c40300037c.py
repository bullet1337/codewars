# https://www.codewars.com/kata/578553c3a1b8d5c40300037c
def binary_array_to_number(arr):
    return int(''.join(str(bit) for bit in arr), 2)
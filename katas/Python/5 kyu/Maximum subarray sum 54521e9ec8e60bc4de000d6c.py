# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
def maxSequence(arr):
    sum = 0
    for i in range(len(arr)):
        current_sum = 0
        for y in arr[i:]:
            current_sum += y
            sum = max(sum, current_sum)
    return sum
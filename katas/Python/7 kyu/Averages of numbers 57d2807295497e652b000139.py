# https://www.codewars.com/kata/57d2807295497e652b000139
def averages(arr):
    return [(arr[i] + arr[i + 1]) / 2 for i in range(len(arr) - 1)] if arr else []
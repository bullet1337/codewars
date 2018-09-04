# https://www.codewars.com/kata/58daa7617332e59593000006
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
# https://www.codewars.com/kata/56b7f2f3f18876033f000307
def in_asc_order(arr):
    return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))
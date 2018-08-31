# https://www.codewars.com/kata/54f8b0c7a58bce9db6000dc4
def rotate(arr, n):
    n %= len(arr)
    return arr[-n:] + arr[:-n]
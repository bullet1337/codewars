# https://www.codewars.com/kata/57f609022f4d534f05000024
def stray(arr):
    return next(c for i, c in enumerate(arr) if c != arr[i - 1] and c != arr[(i + 1) % len(arr)])
# https://www.codewars.com/kata/555b1890a75b930e63000023
def combos(n):
    def helper(arr, sum, element):
        if sum == n:
            return [arr]
        elif sum > n or element > n:
            return []
        else:
            same = helper(arr + arr[-1:], sum + arr[-1], element) if arr and element - arr[-1] <= 1 else []
            next = helper(arr + [element], sum + element, element + 1)
            skip = helper(arr, sum, element + 1)
            return same + next + skip

    return helper([], 0, 1)
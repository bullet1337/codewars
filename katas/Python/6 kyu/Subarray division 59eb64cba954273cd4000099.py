# https://www.codewars.com/kata/59eb64cba954273cd4000099
def solve(arr, n):
    def helper(arr, sum):
        if sum > 0 and sum % n == 0:
            return True

        if len(arr) != 0:
            return helper(arr[1:], sum + arr[0]) or helper(arr[1:], sum)

        return False

    return helper(arr, 0)
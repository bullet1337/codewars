# https://www.codewars.com/kata/51675d17e0c1bed195000001
def solution(digits):
    return int(max(digits[i:i + 5] for i in range(len(digits) - 5 + 1)))
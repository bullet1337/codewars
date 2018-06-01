# https://www.codewars.com/kata/52c31f8e6605bcc646000082
def two_sum(numbers, target):
    return next([i, i + 1 + j] for i, x in enumerate(numbers) for j, y in enumerate(numbers[i + 1:]) if x + y == target)
    
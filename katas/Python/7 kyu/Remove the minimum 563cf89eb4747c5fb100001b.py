# https://www.codewars.com/kata/563cf89eb4747c5fb100001b
def remove_smallest(numbers):
    idx = 0
    if numbers:
        idx = numbers.index(min(numbers))
    return numbers[:idx] + numbers[idx + 1:]

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
def count_positives_sum_negatives(arr):
    return [sum(1 for e in arr if e > 0), sum(e for e in arr if e < 0)] if arr else arr
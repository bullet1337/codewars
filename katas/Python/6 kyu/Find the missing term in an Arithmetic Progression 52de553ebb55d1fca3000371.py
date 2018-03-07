# https://www.codewars.com/kata/52de553ebb55d1fca3000371
def find_missing(sequence):
    for i in range(len(sequence) - 2):
        left_diff = sequence[i + 1] - sequence[i]
        right_diff = sequence[i + 2] - sequence[i + 1]
        if left_diff != right_diff:
            if left_diff > right_diff:
                return sequence[i] + right_diff
            else:
                return sequence[i + 1] + left_diff
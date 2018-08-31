# https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611
def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0

    x = []
    for arr in array_of_arrays:
        if not arr:
            return 0
        x.append(len(arr))
    x.sort()
    return next((l + 1 for i, l in enumerate(x[:-1]) if (l + 1) != x[i + 1]), 0)
    
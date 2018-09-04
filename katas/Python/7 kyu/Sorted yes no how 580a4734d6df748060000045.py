# https://www.codewars.com/kata/580a4734d6df748060000045
def is_sorted_and_how(arr):
    order = arr[0] < arr[1]
    for i in range(2, len(arr)):
        if (order and arr[i] <= arr[i - 1]) or (not order and arr[i] >= arr[i - 1]):
            return "no"
    return 'yes, ascending' if order else 'yes, descending'
            
# https://www.codewars.com/kata/576b93db1129fcf2200001e6
def sum_array(arr):
    return sum(sorted(arr or [])[1:-1])
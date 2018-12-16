# https://www.codewars.com/kata/54466996990c921f90000d61
def is_monotone(heights):
    for h1, h2 in zip(heights, heights[1:]):
        if h1 > h2:
            return False
    return True
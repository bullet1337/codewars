# https://www.codewars.com/kata/550554fd08b86f84fe000a58
def in_array(array1, array2):
    return sorted({s1 for s1 in array1 if any(s1 in s2 for s2 in array2)})
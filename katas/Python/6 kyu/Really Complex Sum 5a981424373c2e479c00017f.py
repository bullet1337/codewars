# https://www.codewars.com/kata/5a981424373c2e479c00017f
def complexSum(arr):
    result = str(sum(complex(number.replace('i', 'j')) for number in arr))\
        .replace('j', 'i').replace('(', '').replace(')', '')

    if len(result) == 2 and result[0] in '01' and result[1] == 'i':
        return 'i' if result[0] != '0' else '0'
    elif len(result) > 2 and result[-3] in '+-' and result[-2] in '01' and result[-1] == 'i':
        return result[:-3] + (result[-3] + 'i' if result[-2] != '0' else '')
    else:
        return result
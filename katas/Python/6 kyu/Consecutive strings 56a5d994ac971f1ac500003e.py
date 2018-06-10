# https://www.codewars.com/kata/56a5d994ac971f1ac500003e
def longest_consec(strarr, k):
    if len(strarr) == 0 or not(0 < k <= len(strarr)):
        return ''
    
    res = ''.join(strarr[:k])
    for i in range(1, len(strarr) - k + 1):
        x = ''.join(strarr[i:i + k])
        if len(x) > len(res):
            res = x
    return res
        
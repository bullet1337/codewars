# https://www.codewars.com/kata/58a65c82586e98266200005b
def fix_progression(arr):
    dd = {}
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = (arr[j] - arr[i]) / (j - i)
            if not diff.is_integer():
                continue
            diff = int(diff)
            dd[diff] = max(dd.get(diff, 0), 2 + sum(1 for k in range(j + 1, len(arr)) if arr[k] == arr[j] + diff * (k - j)))
    return len(arr) - max(dd.values())

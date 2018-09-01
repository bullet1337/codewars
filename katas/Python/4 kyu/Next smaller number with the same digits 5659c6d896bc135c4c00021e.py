# https://www.codewars.com/kata/5659c6d896bc135c4c00021e
def next_smaller(n):
    n = list(str(n))
    for i in range(len(n) - 1, 0, -1):
        if n[i] < n[i - 1]:
            break
    else:
        return -1
    
    rest_max_idx = i + max(enumerate(x for x in n[i:] if x < n[i - 1]), key=lambda x: x[1])[0]
    if i == 1 and n[rest_max_idx] == '0':
        return -1
    n[i - 1], n[rest_max_idx] = n[rest_max_idx], n[i - 1]
    
    return int(''.join(n[:i] + sorted(n[i:], reverse=True)))
# https://www.codewars.com/kata/54d81488b981293527000c8f
def sum_pairs(ints, s):
    ints_map = {}
    dups_map = {}
    for i, n in enumerate(ints):
        if n not in ints_map:
            ints_map[n] = i
        elif n not in dups_map:
            dups_map[n] = i
  
    result = [len(ints), len(ints)]
    for n, i in ints_map.items():
        j = (ints_map if n != s - n else dups_map).get(s - n)
        if j is not None and i != j and max(i, j) < result[1]:
            result = [i, j] if i < j else [j, i]    
    return [ints[result[0]], ints[result[1]]] if result[0] != result[1] else None
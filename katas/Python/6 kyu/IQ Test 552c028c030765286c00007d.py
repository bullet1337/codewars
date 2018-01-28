# https://www.codewars.com/kata/552c028c030765286c00007d
def iq_test(numbers):
    num_map = {0: [], 1: []}
    for i, number in enumerate(numbers.split()):
        num_map[int(number) % 2].append(i + 1)

    for v in num_map.values():
        if len(v) == 1:
            return v[0]
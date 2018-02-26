# https://www.codewars.com/kata/5511b2f550906349a70004e1
last_digit_map = dict.fromkeys(i for i in range(10))
for key in last_digit_map:
    last_digit_map[key] = []
    acc = key
    while acc not in last_digit_map[key]:
        last_digit_map[key].append(acc)
        acc = (acc * key) % 10


def last_digit(n1, n2):
    if n2 == 0:
        return 1

    return last_digit_map[n1 % 10][n2 % len(last_digit_map[n1 % 10]) - 1]
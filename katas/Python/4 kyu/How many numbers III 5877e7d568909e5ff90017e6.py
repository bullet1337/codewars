# https://www.codewars.com/kata/5877e7d568909e5ff90017e6
def find_all(sum_dig, digs):
    numbers = []
    if digs > 0:
        for i in range(9, 0, -1):
            sum = sum_dig - i
            if sum > 0:
                numbers.append((str(i), sum))

    result = [0, None, None]
    while numbers:
        number = numbers.pop()
        if len(number[0]) == digs:
            if number[1] == 0:
                result[0] += 1
                if result[1] is None:
                    result[1] = int(number[0])
                result[2] = int(number[0])
        else:
            for i in range(9, int(number[0][-1]) - 1, -1):
                sum = number[1] - i
                if sum >= 0:
                    numbers.append((number[0] + str(i), sum))
    return [] if result[0] == 0 else result
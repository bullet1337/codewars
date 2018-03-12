# https://www.codewars.com/kata/5a906c895084d7ed740000c2
def solve(n):
    numbers = [1]
    while n > 1:
        temp = [1]
        for i in range(len(numbers) - 1):
            temp.append(temp[-1] + numbers[i + 1])
        temp.append(temp[-1])
        numbers = temp
        n -= 1
    return sum(numbers)
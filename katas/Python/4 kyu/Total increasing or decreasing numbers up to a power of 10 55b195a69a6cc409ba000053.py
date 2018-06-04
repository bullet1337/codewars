# https://www.codewars.com/kata/55b195a69a6cc409ba000053
def total_inc_dec(x):
    stack = [1] * 10
    top = [stack[-1]]
    for _ in range(x):
        for i in range(1, len(stack)):
            stack[i] = stack[i] + stack[i - 1]
        top.append(stack[-1])
    return top[-1] + sum(top[1:]) - x * 10
# https://www.codewars.com/kata/54ca3e777120b56cb6000710
def chained(functions):
    if len(functions) > 1:
        return lambda x: chained(functions[1:])(functions[0](x))
    else:
        return lambda x: functions[0](x)
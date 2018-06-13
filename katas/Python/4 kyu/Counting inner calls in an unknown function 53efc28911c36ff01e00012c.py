# https://www.codewars.com/kata/53efc28911c36ff01e00012c
import sys


def trace_func(frame, event, arg):
    global callers
    if event == 'call' and sys._getframe(2).f_code.co_name in callers:
        global count
        count += 1
        callers.add(sys._getframe(1).f_code.co_name)
        
        
count = 0
callers = set()
sys.settrace(trace_func)


def count_calls(func, *args, **kwargs):
    global count, callers
    count = 0
    callers = {func.__name__}
    rv = func(*args, **kwargs)
    return count, rv

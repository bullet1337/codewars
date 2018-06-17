# https://www.codewars.com/kata/57202aefe8d6c514300001fd
def sale_hotdogs(n):
    return (100 if n < 5 else 95 if n < 10 else 90) * n
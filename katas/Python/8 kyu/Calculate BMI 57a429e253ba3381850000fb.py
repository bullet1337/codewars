# https://www.codewars.com/kata/57a429e253ba3381850000fb
def bmi(weight, height):
    x = weight / height ** 2
    if x <= 18.5: return 'Underweight'
    elif x <= 25.0: return 'Normal'
    elif x <= 30.0: return 'Overweight'
    else: return 'Obese'

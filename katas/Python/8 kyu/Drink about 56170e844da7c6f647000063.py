# https://www.codewars.com/kata/56170e844da7c6f647000063
def people_with_age_drink(age):
    prefix = 'drink '
    postfix = ''
    if age < 14:
        postfix = 'toddy'
    elif age < 18:
        postfix = 'coke'
    elif age < 21:
        postfix = 'beer'
    else:
        postfix = 'whisky'
    return prefix + postfix
# https://www.codewars.com/kata/5827bc50f524dd029d0005f2
def get_first_python(users):
    try:
        return '{p[first_name]}, {p[country]}'.format(p=next(user for user in users if user['language'] == 'Python'))
    except:
        return 'There will be no Python developers'
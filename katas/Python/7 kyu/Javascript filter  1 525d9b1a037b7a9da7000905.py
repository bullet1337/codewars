# https://www.codewars.com/kata/525d9b1a037b7a9da7000905
def search_names(logins):
    return filter(lambda lp: lp[0][-1] == '_', logins)
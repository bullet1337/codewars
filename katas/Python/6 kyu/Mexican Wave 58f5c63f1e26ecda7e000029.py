# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
def wave(str):
    return [str[:i] + str[i].upper() + str[i + 1:] for i in range(len(str)) if str[i].isalpha()]
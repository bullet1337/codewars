# https://www.codewars.com/kata/53af2b8861023f1d88000832
def areYouPlayingBanjo(name):
    return name + (' plays banjo' if name[0].lower() == 'r' else ' does not play banjo')
    
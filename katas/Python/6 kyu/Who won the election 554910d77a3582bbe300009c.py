# https://www.codewars.com/kata/554910d77a3582bbe300009c
from collections import Counter


def getWinner(listOfBallots):
    votes = Counter(listOfBallots).most_common()
    if len(votes) > 1 and votes[0][1] == votes[1][1]:
        return None
    elif votes[0][1] > len(listOfBallots) / 2:
        return votes[0][0]
    else:
        return None
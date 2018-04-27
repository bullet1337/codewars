# https://www.codewars.com/kata/556c04c72ee1147ff20000c9
from collections import defaultdict
from functools import reduce


def valid(a):
    size = len(a[0][0])
    number_of_groups = len(a[0])

    players = defaultdict(set)
    played_today = []
    for day in a:
        played_today.append(set())
        if len(day) != number_of_groups:
            return False

        for group in day:
            if len(group) != size:
                return False

            for player in group:
                if player in played_today[-1]:
                    return False
                else:
                    played_today[-1].add(player)

                for other_player in group:
                    if other_player != player:
                        if other_player in players[player]:
                            return False
                        else:
                            players[player].add(other_player)

    return reduce(lambda x, y: x & y, played_today) == played_today[0]
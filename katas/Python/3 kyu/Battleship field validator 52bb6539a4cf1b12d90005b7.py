# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
from collections import defaultdict


def get_ship(x, y, map, visited):
    points = set()
    next = None
    for i in range(max(0, x - 1), min(x + 2, len(map))):
        for j in range(max(0, y - 1), min(y + 2, len(map))):
            if (i != x or j != y) and map[i][j] == 1 and (i, j) not in visited:
                if i != x and j != y:
                    return None
                else:
                    if next is None:
                        next = (i, j)
                    else:
                        return None
    points.add((x, y))
    visited.add((x, y))
    if next is not None:
        next = get_ship(next[0], next[1], map, visited)
        if next is None:
            return None
        else:
            points |= next
    return points


def validateBattlefield(map):
    visited = set()
    ships = defaultdict(list)
    for x in range(len(map)):
        for y in range(len(map)):
            if map[x][y] == 1 and (x, y) not in visited:
                ship = get_ship(x, y, map, visited)
                if ship is None:
                    return False
                else:
                    ships[len(ship)].append(ship)

    return len(ships[4]) == 1 and len(ships[3]) == 2 and len(ships[2]) == 3 and len(ships[1]) == 4
# https://www.codewars.com/kata/549ee8b47111a81214000941
moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]


def knight(p1, p2):
    goal = [int(p2[1]) - 1, ord(p2[0]) - ord('a')]
    steps = 0
    stack = [[int(p1[1]) - 1, ord(p1[0]) - ord('a')]]
    while True:
        temp = []
        for position in stack:
            if position == goal:
                return steps
            for move in moves:
                if 0 <= position[0] + move[0] <= 7 and 0 <= position[1] + move[1] <= 7:
                    temp.append([position[0] + move[0], position[1] + move[1]])
        stack = temp
        steps += 1
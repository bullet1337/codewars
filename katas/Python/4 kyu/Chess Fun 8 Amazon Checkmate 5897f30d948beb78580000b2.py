# https://www.codewars.com/kata/5897f30d948beb78580000b2
def amazon_check_mate(king, amazon):
    desk = [[0] * 8 for _ in range(8)]

    k_x, k_y = ord(king[0]) - ord('a'), int(king[1]) - 1
    a_x, a_y = ord(amazon[0]) - ord('a'), int(amazon[1]) - 1

    for move in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        x, y = a_x + move[0], a_y + move[1]
        while 0 <= x <= 7 and 0 <= y <= 7 and (x != k_x or y != k_y):
            desk[x][y] = 1
            x += move[0]
            y += move[1]

    for move in [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]:
        if 0 <= a_x + move[0] < 8 and 0 <= a_y + move[1] < 8:
            desk[a_x + move[0]][a_y + move[1]] = 1

    desk[a_x][a_y] = 0

    for i in range(max(0, k_x - 1), min(8, k_x + 2)):
        for j in range(max(0, k_y - 1), min(8, k_y + 2)):
            desk[i][j] = 2

    cm = c = sm = s = 0
    for x in range(8):
        for y in range(8):
            if desk[x][y] == 2 or (x == a_x and y == a_y):
                continue

            if any(desk[i][j] == 0 and (i != x or j != y)
                       for i in range(max(0, x - 1), min(8, x + 2))
                       for j in range(max(0, y - 1), min(8, y + 2))):
                if desk[x][y] == 0:
                    s += 1
                else:
                    c += 1
            elif desk[x][y] == 0:
                sm += 1
            else:
                cm += 1
    return [cm, c, sm ,s]
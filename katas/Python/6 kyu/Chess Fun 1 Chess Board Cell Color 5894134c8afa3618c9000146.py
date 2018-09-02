# https://www.codewars.com/kata/5894134c8afa3618c9000146
def chess_board_cell_color(cell1, cell2):
    return ((ord(cell1[0]) - ord('A')) % 2 == (ord(cell2[0]) - ord('A')) % 2) == (int(cell1[1]) % 2 == int(cell2[1]) % 2)
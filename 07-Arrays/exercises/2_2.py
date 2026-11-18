###
# Wypisuje planszę do kółko i krzyżyk
#
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# pętla zewnętrzna bierze kolejne wiersze, wewnętrzna kolejne pola w wierszu
for row in tic_tac_toe_board:
    for cell in row:
        # end=" " - po wypisaniu pola nie przechodzimy do nowej linii
        print(cell, end=" ")
    # po całym wierszu przechodzimy do nowej linii
    print()

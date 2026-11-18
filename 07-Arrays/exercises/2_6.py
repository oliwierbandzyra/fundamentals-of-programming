###
# Wpisuje 1 na głównej przekątnej macierzy kwadratowej
#
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# na głównej przekątnej numer wiersza i kolumny są takie same: [0][0], [1][1], [2][2]
for i in range(len(matrix)):
    matrix[i][i] = 1

# wypisanie macierzy
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

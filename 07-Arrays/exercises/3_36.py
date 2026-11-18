###
# Macierz jednostkowa (jedynki na przekątnej, reszta zer)
#

# Zwraca macierz jednostkową n x n
def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            # jedynka tylko tam, gdzie numer wiersza równa się numerowi kolumny
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

# Wypisuje tablicę 2D w wierszach i kolumnach
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

for size in [3, 5, 8]:
    print_matrix(identity_matrix(size))
    print()

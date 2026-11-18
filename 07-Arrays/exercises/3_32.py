###
# Tworzy tabliczkę mnożenia 5x5
#
arr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# i to numer wiersza, j to numer kolumny (liczone od 0, więc dodajemy 1)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = (i + 1) * (j + 1)

for row in arr:
    for value in row:
        # :3 oznacza, że każda liczba zajmuje 3 znaki, dzięki temu kolumny są równe
        print(f'{value:3}', end="")
    print()

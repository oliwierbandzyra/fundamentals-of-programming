###
# Wypisuje zawartość tablicy w odwrotnej kolejności
#
arr = [15, 8, 31, 47, 2, 19]

print('existed array:', end=" ")
for value in arr:
    print(value, end=" ")
print()

print('reverse array:', end=" ")
# range(start, stop, krok): zaczynamy od ostatniego indeksu,
# idziemy do 0 (stop = -1, bo stop nie jest wliczany), krok -1 w dół
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()

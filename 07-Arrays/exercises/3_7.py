###
# Średnia arytmetyczna elementów tablicy (pętla for)
#
arr = [15, 8, 31, 47, 2, 19]

print('Array:', arr)

total = 0
for value in arr:
    total = total + value

# średnia = suma / liczba elementów
mean = total / len(arr)
print('Arithmetic mean:', round(mean, 2))

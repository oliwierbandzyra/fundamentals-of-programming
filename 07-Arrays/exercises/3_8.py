###
# Średnia arytmetyczna elementów tablicy (pętla while)
#
arr = [15, 8, 31, 47, 2, 19]

print('Array:', arr)

total = 0
i = 0
while i < len(arr):
    total = total + arr[i]
    i = i + 1

mean = total / len(arr)
print('Arithmetic mean:', round(mean, 2))

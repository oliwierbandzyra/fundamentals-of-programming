###
# Modyfikuje wartości w tablicy i wypisuje ją po każdej zmianie
#
arr = [1, 2, 3, 4, 5]
print('Array:', arr)

# odejmujemy 1 od pierwszego elementu
arr[0] = arr[0] - 1
print('Array:', arr)

# zwiększamy ostatni element o 4
arr[len(arr) - 1] = arr[len(arr) - 1] + 4
print('Array:', arr)

# mnożymy środkowy element przez 2
arr[len(arr) // 2] = arr[len(arr) // 2] * 2
print('Array:', arr)

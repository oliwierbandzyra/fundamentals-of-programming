###
# Wypisuje wybrane elementy tablicy (listy)
#
arr = [2, 3, 7, 5, 4]

print(arr)
# len() zwraca liczbę elementów listy
print('Number of elements', len(arr))
# indeksy w liście liczymy od 0, więc pierwszy element to arr[0]
print('First value', arr[0])
print('Second value', arr[1])
# ostatni element ma indeks arr[len(arr) - 1] lub arr[-1]
print('Last value', arr[-1])
# przedostatni element ma indeks arr[len(arr) - 2] lub arr[-2]
print('Last but one value', arr[-2])
print('Sum of the first and last value', arr[0] + arr[-1])
# środkowy element: // to dzielenie całkowite, 5 // 2 = 2, czyli trzeci element
print('Middle value', arr[len(arr) // 2])

# wszystkie wartości w jednej linii, oddzielone spacją (end=" " zamiast nowej linii)
print('All values:', end=" ")
for value in arr:
    print(value, end=" ")
print()

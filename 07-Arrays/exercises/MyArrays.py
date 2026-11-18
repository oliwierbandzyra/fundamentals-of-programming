###
# Moduł z funkcjami do operacji na tablicach liczb
# (bez użycia wbudowanych funkcji min, max, sorted, sum)
#

# Zwraca drugi największy element tablicy
def second_largest(arr):
    # first - największy dotąd, second - drugi największy dotąd
    first = arr[0]
    second = arr[1]
    # jeśli drugi jest większy od pierwszego, zamieniamy je
    if second > first:
        temp = first
        first = second
        second = temp
    # sprawdzamy resztę elementów (od indeksu 2)
    for i in range(2, len(arr)):
        if arr[i] > first:
            # nowy największy, dotychczasowy największy staje się drugim
            second = first
            first = arr[i]
        elif arr[i] > second:
            second = arr[i]
    return second

# Zwraca różnicę między największą a najmniejszą wartością
def difference(arr):
    maximum = arr[0]
    minimum = arr[0]
    for value in arr:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
    return maximum - minimum

# Zwraca medianę (środkową wartość po posortowaniu)
def median(arr):
    # robimy kopię, żeby nie zmienić kolejności w oryginalnej tablicy
    copy = []
    for value in arr:
        copy.append(value)
    # sortowanie bąbelkowe kopii
    n = len(copy)
    for i in range(n):
        for j in range(n - i - 1):
            if copy[j] > copy[j + 1]:
                temp = copy[j]
                copy[j] = copy[j + 1]
                copy[j + 1] = temp
    # nieparzysta liczba elementów - bierzemy środkowy
    if n % 2 == 1:
        return copy[n // 2]
    # parzysta liczba elementów - średnia z dwóch środkowych
    return (copy[n // 2 - 1] + copy[n // 2]) / 2

# Zwraca dwuelementową tablicę [najmniejsza, największa]
def smallest_and_largest(arr):
    maximum = arr[0]
    minimum = arr[0]
    for value in arr:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
    return [minimum, maximum]

# Zwraca elementy tablicy jako tekst oddzielony znakiem minus
def to_minus_string(arr):
    result = ''
    for i in range(len(arr)):
        if i > 0:
            result = result + '-'
        # f'{...}' wstawia wartość do tekstu
        result = result + f'{arr[i]}'
    return result

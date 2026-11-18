###
# Wypisuje wartości tablicy w formie graficznej (gwiazdki)
#

# Zwraca podaną liczbę gwiazdek jako tekst
def star(n):
    # '*' * n powtarza gwiazdkę n razy
    return '*' * n

arr = [2, 6, 4, 9, 7]
for number in arr:
    print(str(number) + ': ' + star(number))

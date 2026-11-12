# Tworzymy dwie pierwsze liczby ciągu Fibonacciego: a = 0 oraz b = 1
a, b = 0, 1
# Pętla for wykona się 20 razy, aby wypisać 20 pierwszych wyrazów ciągu
for i in range(20):
    # Wypisujemy aktualną wartość zmiennej a w jednej linii, oddzielając liczby spacją
    print(a, end=" ")
    # Jednocześnie aktualizujemy zmienne: nowa wartość 'a' to stare 'b', a nowa wartość 'b' to suma poprzednich 'a + b'
    a, b = b, a + b

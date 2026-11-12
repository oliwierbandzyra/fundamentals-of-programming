# Pętla for generuje kolejne liczby całkowite od 1 do 30 włącznie
for i in range(1, 31):
    # Najpierw sprawdzamy, czy liczba dzieli się jednocześnie przez 3 ORAZ przez 5 (np. 15, 30)
    if i % 3 == 0 and i % 5 == 0:
        # Wypisujemy 'BINGO' i zamiast przechodzić do nowej linii, stawiamy spację (end=" ")
        print("BINGO", end=" ")
    # W przeciwnym razie, jeśli liczba dzieli się tylko przez 3
    elif i % 3 == 0:
        # Wypisujemy 'THREE' ze spacją na końcu
        print("THREE", end=" ")
    # W przeciwnym razie, jeśli liczba dzieli się tylko przez 5
    elif i % 5 == 0:
        # Wypisujemy 'FIVE' ze spacją na końcu
        print("FIVE", end=" ")
    # W każdym innym przypadku (gdy liczba nie dzieli się ani przez 3, ani przez 5)
    else:
        # Wypisujemy po prostu samą liczbę i ze spacją na końcu
        print(i, end=" ")

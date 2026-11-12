# Zewnętrzna pętla odpowiada za wiersze kuponu totolotka (numery wierszy od 1 do 7)
for row in range(1, 8):
    # Wewnętrzna pętla odpowiada za kolumny w danym wierszu (indeksy kolumn od 0 do 6, czyli 7 kolumn)
    for col in range(7):
        # Obliczamy liczbę (row + col*7) i formatujemy ją na szerokość 2 znaków (:2), aby kolumny były równo wyrównane
        print(f"{row + col*7:2}", end=" ")
    # Po wypisaniu wszystkich 7 liczb w wierszu przechodzimy do nowej linii
    print()

# Ustawiamy początkową wartość zmiennej i na 6 (będzie odpowiadać za pierwszy element wiersza klawiatury numerycznej)
i = 6
# Zewnętrzna pętla while działa dopóki i jest większe lub równe 0 (wykona się dla i = 6, 3, 0)
while i >= 0:
    # Ustawiamy licznik kolumn j na 1 przed każdym nowym wierszem
    j = 1
    # Wewnętrzna pętla while wypisuje 3 liczby w jednym wierszu (dla j = 1, 2, 3)
    while j <= 3: 
        # Wypisujemy sumę i + j (np. dla i=6 będą to: 7, 8, 9) oddzieloną spacją (end=' ')
        print(f'{i+j}', end=' ')
        # Zwiększamy licznik kolumn j o 1
        j += 1
    # Pusty print() przenosi kursor do nowej linii po wypisaniu całego wiersza z 3 liczbami
    print()
    # Zmniejszamy i o 3, aby w kolejnym obiegu wypisać niższy wiersz klawiatury (4 5 6, a potem 1 2 3)
    i -= 3

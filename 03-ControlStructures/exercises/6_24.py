# Pierwsza pętla rysuje górną część wzoru (rosnącą): i przyjmuje wartości 1, 2, 3, 4, 5
for i in range(1, 6):
    # Mnożenie tekstu "* " przez liczbę i powtarza ten tekst i razy w jednej linii
    print("* " * i) 
# Druga pętla rysuje dolną część wzoru (malejącą): range(4, 0, -1) odlicza w dół od 4 do 1 (krok -1)
for i in range(4, 0, -1):
    # Wypisujemy gwiazdki ze spacją powtórzone i razy
    print("* " * i)

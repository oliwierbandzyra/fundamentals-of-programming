# Tworzymy zmienną sum na sumę liczb parzystych i ustawiamy ją na 0
sum = 0
# Pętla for przechodzi przez liczby od 1 do 10 włącznie
for i in range(1, 11):
    # Sprawdzamy, czy liczba i NIE jest parzysta (reszta z dzielenia przez 2 nie jest równa 0)
    if not i % 2 == 0:
        # Instrukcja continue przerywa bieżący krok pętli i natychmiast przechodzi do kolejnej liczby i (pomija dodawanie)
        continue
    # Ta linijka wykona się tylko dla liczb parzystych — dodajemy liczbę i do sumy
    sum += i
# Wyświetlamy obliczoną sumę liczb parzystych z przedziału od 1 do 10
print(f'Sum of even numbers in the range <1,10> is {sum}')

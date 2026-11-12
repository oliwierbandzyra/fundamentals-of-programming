# Ustalamy górną granicę przedziału N równą 10
N = 10
# Tworzymy zmienną sum_even na sumę liczb parzystych i ustawiamy ją na 0
sum_even = 0
# Tworzymy licznik pętli i zaczynając od liczby 1
i = 1
# Pętla while wykonuje się dopóki licznik i jest mniejszy lub równy N (czyli 10)
while i <= N:
    # Sprawdzamy, czy aktualna liczba i jest parzysta (reszta z dzielenia przez 2 wynosi 0)
    if i % 2 == 0:
        # Jeśli jest parzysta, dodajemy ją do zmiennej sum_even
        sum_even += i
    # Zwiększamy licznik i o 1, aby przejść do kolejnej liczby (bardzo ważne, by pętla nie była nieskończona!)
    i += 1 
# Po zakończeniu pętli wyświetlamy wynikową sumę liczb parzystych
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

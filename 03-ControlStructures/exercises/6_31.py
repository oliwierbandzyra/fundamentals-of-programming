# Importujemy moduł random do generowania liczb losowych
import random
# Pętla for wykona się 20 razy (znak '_' oznacza zmienną pomocniczą, której wartości nie używamy wewnątrz pętli)
for _ in range(20): 
    # Losujemy liczbę całkowitą z przedziału od 5 do 10 włącznie i wypisujemy ją obok poprzedniej ze spacją
    print(random.randint(5, 10), end=" ")

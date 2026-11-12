# Importujemy wbudowany moduł time, który pozwala m.in. zatrzymać program na określoną liczbę sekund
import time
# Pobieramy od użytkownika czas odliczania w sekundach jako liczbę całkowitą
t = int(input("Enter time in seconds: "))
# Pętla while działa tak długo, jak pozostały czas t jest większy od 0
while t > 0:
    # Jeśli zostało 5 sekund, wypisujemy słownie 'five'
    if t == 5:
        print("five")
    # Jeśli zostały 4 sekundy, wypisujemy słownie 'four'
    elif t == 4:
        print("four")
    # Jeśli zostały 3 sekundy, wypisujemy słownie 'three'
    elif t == 3:
        print("three")
    # Jeśli zostały 2 sekundy, wypisujemy słownie 'two'
    elif t == 2:
        print("two")
    # Jeśli została 1 sekunda, wypisujemy słownie 'one'
    elif t == 1:
        print("one")
    # Dla wszystkich pozostałych wartości większych niż 5
    else:
        # Wypisujemy po prostu liczbę sekund
        print(t)
    # Zmniejszamy licznik czasu t o 1 sekundę
    t -= 1
    # Usypiamy program na 1 sekundę, aby odliczanie odbywało się w czasie rzeczywistym
    time.sleep(1)
# Gdy czas dojdzie do 0 i pętla się skończy, wyświetlamy komunikat końcowy
print("Time is up!")

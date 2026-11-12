# Tworzymy zmienną total_sum do przechowywania sumy podanych liczb (startujemy od 0)
total_sum = 0
# Tworzymy licznik count do zliczania, ile liczb podał użytkownik (startujemy od 0)
count = 0
# Tworzymy nieskończoną pętlę while True (będzie działać, dopóki sami jej nie przerwiemy instrukcją break)
while True:
    # Pobieramy liczbę całkowitą od użytkownika (0 oznacza koniec wpisywania)
    number = int(input("Enter a number (0 to stop): "))
    # Jeśli użytkownik wpisał 0
    if number == 0:
        # Instrukcja break natychmiast przerywa i kończy działanie pętli while
        break
    # Dodajemy wpisaną liczbę do sumy całkowitej
    total_sum += number
    # Zwiększamy licznik podanych liczb o 1
    count += 1
# Wyświetlamy sumę wszystkich wpisanych liczb
print(f"The total sum of the numbers is: {total_sum}")
# Sprawdzamy, czy użytkownik podał przynajmniej jedną liczbę (żeby uniknąć dzielenia przez zero)
if count > 0:
    # Obliczamy średnią arytmetyczną, dzieląc sumę przez ilość liczb
    mean = total_sum / count
    # Wyświetlamy obliczoną średnią arytmetyczną
    print(f"Arithmetic mean: {mean}")

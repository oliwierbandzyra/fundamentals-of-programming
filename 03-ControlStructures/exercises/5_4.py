# Importujemy wbudowany moduł random, który pozwala losować liczby
import random
# Losujemy tajną liczbę całkowitą z przedziału od 1 do 100 włącznie i zapisujemy w number_to_guess
number_to_guess = random.randint(1, 100)
# Tworzymy zmienną user_guess (strzał użytkownika) i ustawiamy na 0 (liczba spoza zakresu 1-100, więc pętla na pewno wystartuje)
user_guess = 0
# Wyświetlamy instrukcję dla gracza
print("Guess the number between 1 and 100!")
# Pętla while działa tak długo, jak długo strzał użytkownika różni się (!=) od wylosowanej liczby
while user_guess != number_to_guess:
    # Pobieramy liczbę od gracza i zamieniamy na typ całkowity (int)
    user_guess = int(input("Enter your guess: "))
    # Jeśli podana liczba jest mniejsza od szukanej
    if user_guess < number_to_guess:
        # Podpowiadamy, że liczba jest za mała
        print("Too low! Try again.")
    # W przeciwnym razie, jeśli podana liczba jest większa od szukanej
    elif user_guess > number_to_guess:
        # Podpowiadamy, że liczba jest za duża
        print("Too high! Try again.")
    # W przeciwnym razie (gdy liczby są równe)
    else:
        # Gratulujemy odgadnięcia liczby (po tym kroku warunek pętli while stanie się fałszywy i pętla się zakończy)
        print("Congratulations! You guessed the correct number.")

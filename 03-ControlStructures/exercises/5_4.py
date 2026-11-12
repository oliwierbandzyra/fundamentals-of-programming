import random

# Losujemy tajną liczbę z zakresu 1–100 włącznie
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

# Powtarzamy zgadywanie dopóki strzał użytkownika różni się od wylosowanej liczby
while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

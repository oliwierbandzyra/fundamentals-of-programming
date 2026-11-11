###
# A program that checks whether the number entered from the keyboard is even.
#

# wpisanie liczby całkowitej z klawiatury
number = int(input('Enter number: '))

# Reszta z dzielenia przez 2 równa 0 oznacza liczbę parzystą
even = (number % 2 == 0)
# wypisanie czy liczba parzysta
print(f'Number is even: {even}')
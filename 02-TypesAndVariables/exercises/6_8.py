###
# A program that calculates how many letters are between two given letters
#

first = input('Enter first letter: ')
last = input('Enter last letter: ')

# Pobieramy kody ASCII z ord() obu liter i obliczamy różnicę pomniejszoną o 1 i usuwamy ewentualny minus
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = abs(last_letter_code - first_letter_code) - 1

# Wypisanie z pomocą f-string wyniku
print(f'Between {first} and {last} is {number_of_letters} letters')
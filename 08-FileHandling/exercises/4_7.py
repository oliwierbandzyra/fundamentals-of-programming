###
# Liczy samogłoski w tekście wpisanym z klawiatury
#
import re

text = input('Enter text: ')

# [aeiou] - dowolna z samogłosek
# re.IGNORECASE - nie rozróżniamy wielkich i małych liter
# findall() zwraca listę wszystkich znalezionych samogłosek
vowels = re.findall('[aeiou]', text, re.IGNORECASE)

# liczba samogłosek to długość tej listy
print('Number of vowels:', len(vowels))

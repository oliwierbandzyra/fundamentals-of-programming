###
# A program that reads an integer and prints its binary and hexadecimal representation.
#

#wypisanie z klawiatury liczby
number = int(input('Enter number: '))

# Z użyciem f-stringa wkładamy wartość zmiennej i Używamy wbudowanych funkcji bin() oraz hex() do konwersji systemu liczbowego
print(f'Binary number: {bin(number)}')
print(f'Hexadecimal number: {hex(number)}')
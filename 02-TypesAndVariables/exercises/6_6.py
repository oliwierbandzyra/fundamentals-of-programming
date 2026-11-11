###
# A program to print numerical representations of characters.
#

chars = ['a', 'b', 'z', 'A', 'B', 'Z', '1', '=', '+', '€']

# Iterujemy po liście znaków za pomocą pętli for i wypisujemy ich kod numeryczny ASCII za pomocą ord()
for ch in chars:
    print(f'{ch} {ord(ch)}')
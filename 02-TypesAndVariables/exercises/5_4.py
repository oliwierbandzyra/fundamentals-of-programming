###
# A program that reads an amount and calculates VAT 23%
#

# Wczytujemy kwotę jako liczbę zmiennoprzecinkową
amount = float(input('Enter amount: '))

# Obliczamy 23% podatku VAT
vat = amount * 0.23

# Wyświetlamy sformatowane wyniki z dokładnością do dwóch miejsc po przecinku (:.2f)
print(f'Amount  : {amount:.2f}') # instrukcja formatowania liczby wewnątrz nawiasu klamrowego. Dwukropek rozpoczyna formatowanie, .2 oznacza dwa miejsca po przecinku, a f oznacza liczbę zmiennoprzecinkową (ułamek dziesiętny).
print(f'VAT 23% : {vat:.2f}')
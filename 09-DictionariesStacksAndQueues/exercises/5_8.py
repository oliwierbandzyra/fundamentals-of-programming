###
# Oblicza łączny koszt koszyka zakupów na podstawie cennika
#

# Cennik: produkt -> cena za sztukę
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Koszyk: produkt -> liczba sztuk
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Obliczenie łącznego kosztu
total = 0
for product, quantity in cart.items():
    # prices[product] to cena jednej sztuki (szukamy jej w cenniku po nazwie)
    total += prices[product] * quantity

print('Total cost of the shopping cart:', round(total, 2))

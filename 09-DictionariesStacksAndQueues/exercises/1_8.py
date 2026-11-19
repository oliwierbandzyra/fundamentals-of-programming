###
# Obniżka cen o 10% w sklepie z odzieżą
#
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# Funkcja wypisuje listę produktów z cenami i zwraca ich łączną wartość
def print_prices(prices):
    total = 0
    for product, price in prices.items():
        print(f'{product} : {price}')
        total += price
    return round(total, 2) # round zaokrągla do 2 miejsc po przecinku

print('PRICES BEFORE THE DISCOUNT')
total_before = print_prices(price_list)
print('Total value before the discount:', total_before)

# Zmiana cen w słowniku: nowa cena to 90% starej (obniżka o 10%)
# Podczas zmiany wartości przechodzimy po kluczach słownika
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

print()
print('PRICES AFTER THE 10% DISCOUNT')
total_after = print_prices(price_list)
print('Total value after the discount:', total_after)

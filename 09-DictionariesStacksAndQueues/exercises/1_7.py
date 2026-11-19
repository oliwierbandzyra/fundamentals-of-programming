###
# Produkty w sklepie komputerowym: lista i łączna liczba sztuk
#
products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

total = 0 # tu zliczamy wszystkie sztuki
print('PRODUCTS IN THE STORE')
for product, quantity in products.items():
    print(f'{product} : {quantity}')
    total += quantity # dodajemy liczbę sztuk tego produktu do sumy

print('Total number of products:', total)

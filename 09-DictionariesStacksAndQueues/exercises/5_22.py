###
# Zapisuje dane kupionego produktu do pliku product.json
#
import json

product = {}

# Odczyt danych produktu z klawiatury.
# Ważne są typy danych: nazwa to tekst (str), cena to liczba (float),
# a "paid" to wartość logiczna (bool: true/false w pliku json)
product['name'] = input('Product name: ')
product['price'] = float(input('Price: ')) # float() zamienia tekst na liczbę rzeczywistą
answer = input('Paid (yes/no): ')
# porównanie daje od razu True (jeśli wpisano yes) albo False
product['paid'] = answer.lower() == 'yes'

# Zapis danych produktu do pliku json
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print('Product data has been saved to product.json')

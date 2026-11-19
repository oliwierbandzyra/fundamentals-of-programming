###
# Wypisuje produkty z pliku clothing.csv, których cena < 60 i stan magazynowy < 40
#
import csv

# Funkcja szuka w nagłówku numeru kolumny, której nazwa zawiera dane słowo
def find_column(header, word):
    for i in range(len(header)):
        if word in header[i].lower():
            return i

with open('clothing.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    price_col = find_column(header, 'price')
    stock_col = find_column(header, 'stock')

    # wypisujemy też nagłówek, żeby było wiadomo, co oznaczają kolumny
    print(','.join(header))
    for row in reader:
        # wartości w CSV są tekstami, więc zamieniamy je na liczby (float)
        price = float(row[price_col])
        stock = float(row[stock_col])
        if price < 60 and stock < 40:
            print(','.join(row))

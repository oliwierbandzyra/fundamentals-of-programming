###
# Podsumowanie rezerwacji pokoi w hotelu (plik reservations.json)
# Program jest podzielony na funkcje
#
import json

# Wczytuje rezerwacje z pliku i zwraca listę rezerwacji
def read_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file) # słownik z kluczem "reservations"
    return data['reservations'] # lista słowników - jedna rezerwacja to jeden pokój

# Zwraca liczbę zarezerwowanych pokoi
def count_rooms(reservations):
    return len(reservations)

# Zwraca liczbę rezerwacji opłaconych (paid=True) albo nieopłaconych (paid=False)
def count_reservations(reservations, paid):
    counter = 0
    for reservation in reservations:
        if reservation['paid'] == paid:
            counter += 1
    return counter

# Zwraca łączną wartość rezerwacji opłaconych albo nieopłaconych
def total_value(reservations, paid):
    total = 0
    for reservation in reservations:
        if reservation['paid'] == paid:
            # wartość rezerwacji = liczba nocy * cena za noc
            total += reservation['nights'] * reservation['price_per_night']
    return total

# Główna część programu
reservations = read_reservations('reservations.json')

print('RESERVATIONS SUMMARY')
print('Number of rooms:', count_rooms(reservations))
print('Number of paid reservations:', count_reservations(reservations, True))
print('Number of unpaid reservations:', count_reservations(reservations, False))
print('Total value of paid reservations:', total_value(reservations, True))
print('Total value of unpaid reservations:', total_value(reservations, False))

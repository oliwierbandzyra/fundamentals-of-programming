# Ustawiamy stan pierwszego włącznika światła na False (wyłączony)
light_switch1 = False 
# Ustawiamy stan drugiego włącznika światła na False (wyłączony)
light_switch2 = False
# Tworzymy licznik zapalonych żarówek i ustawiamy go na 0
bulbs_on = 0
# Jeśli pierwszy włącznik jest włączony (ma wartość True)
if light_switch1:
    # Pierwszy włącznik zapala 1 żarówkę, więc dodajemy 1 do licznika
    bulbs_on += 1
# Jeśli drugi włącznik jest włączony (ma wartość True) - używamy osobnego 'if', bo oba włączniki działają niezależnie
if light_switch2:
    # Drugi włącznik zapala 2 żarówki, więc dodajemy 2 do licznika
    bulbs_on += 2
# Wyświetlamy łączną liczbę zapalonych żarówek
print(f"Number of bulbs lit: {bulbs_on}")

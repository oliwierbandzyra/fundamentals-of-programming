###
# Sprawdza, która kategoria wydatków była najdroższa
#
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# zakładamy, że najdroższa jest pierwsza kategoria (indeks 0)
max_index = 0
for i in range(len(expenses)):
    # jeśli znajdziemy większy wydatek, zapamiętujemy jego indeks
    if expenses[i] > expenses[max_index]:
        max_index = i

# kategorie i wydatki leżą na tych samych indeksach w obu listach
print('The most expensive category is', categories[max_index], 'with', expenses[max_index])

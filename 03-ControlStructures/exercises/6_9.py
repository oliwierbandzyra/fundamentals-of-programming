# Pobieramy od użytkownika imię i zapisujemy w zmiennej name
name = input("Enter name: ")
# Indeks [-1] oznacza ostatni znak w napisie; sprawdzamy, czy imię kończy się na literę 'a'
if name[-1] == 'a':
    # Jeśli kończy się na 'a', wyświetlamy informację, że to polskie imię żeńskie
    print(f"{name} -- Polish female name")

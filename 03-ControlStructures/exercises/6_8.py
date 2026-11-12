# Pobieramy imię pierwszej osoby
person1_name = input('Enter first person name: ')
# Pobieramy wiek pierwszej osoby jako liczbę całkowitą
person1_age = int(input('Enter first person age: '))
# Pobieramy imię drugiej osoby
person2_name = input('Enter second person name: ')
# Pobieramy wiek drugiej osoby jako liczbę całkowitą
person2_age = int(input('Enter second person age: '))
# Sprawdzamy, czy pierwsza osoba ma co najmniej 18 lat ORAZ (and) druga osoba ma co najmniej 18 lat
if person1_age >= 18 and person2_age >= 18:
    # Jeśli obie są pełnoletnie, wyświetlamy stosowny komunikat
    print(f'Both {person1_name} and {person2_name} are adults')
# W przeciwnym razie (gdy przynajmniej jedna z osób ma mniej niż 18 lat)
else:
    # Informujemy, że jedna z osób (lub obie) nie jest pełnoletnia
    print(f'Either {person1_name} or {person2_name} is not an adult')

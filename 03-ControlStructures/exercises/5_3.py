# Tworzymy zmienną name i przypisujemy jej pusty tekst ''
name = ''
# Pętla while powtarza się dopóki zmienna name jest pusta (czyli użytkownik nic nie wpisał i wcisnął tylko Enter)
while name == '':
    # Prosimy użytkownika o wpisanie imienia
    name = input('Enter your name: ')
# Gdy pętla się zakończy (użytkownik wpisał imię), wyświetlamy powitanie
print(f'Hello {name}')

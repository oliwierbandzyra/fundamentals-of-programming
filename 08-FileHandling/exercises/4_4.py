###
# Wypisuje plik it_company.csv po pięć linii, czekając na klawisz Enter
#
with open('it_company.csv', 'r') as file:
    lines = file.read().splitlines()

i = 0 # numer pierwszej linii w aktualnej porcji
while i < len(lines):
    # wypisujemy pięć kolejnych linii (albo mniej, jeśli plik się kończy)
    for j in range(i, min(i + 5, len(lines))):
        print(lines[j])
    i += 5
    # jeśli są jeszcze linie, czekamy na Enter
    if i < len(lines):
        print('Press Enter key...')
        # input() czeka, aż użytkownik naciśnie Enter
        input()

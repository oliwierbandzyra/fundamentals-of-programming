###
# Oblicza łączną wartość wydanych pieniędzy
#
import re # moduł do wyrażeń regularnych

# nazwa pliku z raportem zakupów
email_file = 'report.txt'

# wczytanie treści e-maila
# encoding='utf-8' jest potrzebne, żeby poprawnie wczytać znak €
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# wzorzec wyrażenia regularnego dla kwot:
# €       - znak euro
# \s?     - opcjonalna spacja
# (...)   - nawias oznacza część, którą chcemy wyciągnąć
# \d+     - jedna lub więcej cyfr
# (\.\d+)? - opcjonalna część dziesiętna: kropka i cyfry
pattern = r'€\s?(\d+(?:\.\d+)?)'

# findall() zwraca listę wszystkich znalezionych kwot (jako teksty)
amounts = re.findall(pattern, email)

# sumowanie zakupów
total = 0
for amount in amounts:
    # float() zamienia tekst na liczbę
    total += float(amount)

# wypisanie wyniku (round zaokrągla do 2 miejsc po przecinku)
print('Amounts found:', amounts)
print(f'Total money spent: €{total:.2f}')

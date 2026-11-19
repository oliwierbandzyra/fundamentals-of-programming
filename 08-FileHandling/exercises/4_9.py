###
# Wypisuje imię, nazwisko i e-mail grafików (Graphic Designer) z pliku it_company.csv
#
import csv # moduł do wygodnej pracy z plikami CSV

# Funkcja szuka w nagłówku numeru kolumny, której nazwa zawiera dane słowo
def find_column(header, word):
    for i in range(len(header)):
        if word in header[i].lower():
            return i

job_title = 'Graphic Designer'

print('GRAPHIC DESIGNERS')
print('=================')

with open('it_company.csv', 'r', newline='') as file:
    # csv.reader dzieli każdą linię na listę wartości (po przecinkach)
    reader = csv.reader(file)
    # pierwsza linia to nagłówek z nazwami kolumn
    header = next(reader)
    first_name_col = find_column(header, 'first')
    last_name_col = find_column(header, 'last')
    email_col = find_column(header, 'email')
    job_col = find_column(header, 'job')

    for row in reader:
        # wybieramy tylko osoby z szukanym stanowiskiem
        if row[job_col] == job_title:
            print(row[first_name_col], row[last_name_col] + ',' + row[email_col])

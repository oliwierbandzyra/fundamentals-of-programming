###
# Zapisuje do pliku listę pracowników zatrudnionych na określonym stanowisku
#

# nazwy plików
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Stanowisko
job_title = 'Software Engineer'

# otwieramy jednocześnie plik do odczytu i plik do zapisu
with open(employees_file, 'r') as source:
    with open(position_file, 'w') as target:
        for line in source:
            # jeśli linia zawiera nazwę stanowiska, zapisujemy ją do nowego pliku
            if job_title in line:
                # linia ma już znak nowej linii, więc nie dodajemy \n
                target.write(line)

print('Employees have been saved to', position_file)

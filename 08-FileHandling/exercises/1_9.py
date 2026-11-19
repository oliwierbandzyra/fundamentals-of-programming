###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
    number = 1 # numer na wypisywanej liście
    for line in file:
        # operator 'in' sprawdza, czy tekst stanowiska jest w linii
        if job_title in line:
            print(f'{number}. {line}', end="")
            number += 1

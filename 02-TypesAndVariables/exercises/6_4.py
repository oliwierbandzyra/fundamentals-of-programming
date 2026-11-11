###
# A program for printing detailed information.
#

employee = "Mr. John May, born on 1998-02-16"

# Wypisujemy z pomocą f-string Używamy wycinków (slicing), aby wyciągnąć konkretne fragmenty tekstu
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[21:]}')
print(f'Initials: {employee[4]}{employee[9]}')
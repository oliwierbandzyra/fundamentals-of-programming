###
# Pozwala wprowadzić i wypisać dane pracownika. Ze względu na ochronę
# danych osobowych można zdecydować, czy pensja zostanie wypisana
#
import keyboard # nasz własny moduł (plik keyboard.py)

# Wczytanie danych pracownika z klawiatury
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')

# Wypisanie karty pracownika
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name:', last_name)
print('Age:', age)
# pensję pokazujemy tylko wtedy, gdy NIE została ukryta
if not is_salary_hidden:
    print('Salary:', salary)

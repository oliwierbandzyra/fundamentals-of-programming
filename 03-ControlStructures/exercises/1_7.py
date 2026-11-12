###
# Program that calculates the employee's salary, taking into account a bonus.
#

basic_salary = 5000
total_salary = 0
bonus = 0.30 # 30% bonusu wspomnianego w treści

# Zapisanie True jeśli użytkownik wpisze "Y"
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

if is_bonus:
    # Obliczenie wynagrodzenia podstawowego powiększonego o bonus
    total_salary = basic_salary + (basic_salary * bonus)
else:
    # Tylko wynagrodzenie podstawowe
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')
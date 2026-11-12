basic_salary = 5000
bonus = 0.30 
# od razu zapisuje True albo False zalezy czy wpisze Y
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'
if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')

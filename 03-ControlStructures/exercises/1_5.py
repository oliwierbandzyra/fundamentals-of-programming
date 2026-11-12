###
# Checking whether the test is passed
#

total_tasks = 20

# Pobranie liczby poprawnie wykonanych zadań
tasks_ok = int(input('Enter number of correctly completed tasks: '))

# Domyślnie test nie jest zdany
test_passed = False

# Warunek zdania testu to min. 50% poprawnych odpowiedzi
if tasks_ok >= total_tasks * 0.5:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
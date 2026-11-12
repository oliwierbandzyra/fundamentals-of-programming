# Ustalamy podstawową pensję równą 5000 i zapisujemy w zmiennej basic_salary
basic_salary = 5000
# Ustalamy wysokość premii na 30% (zapisane jako ułamek dziesiętny 0.30) w zmiennej bonus
bonus = 0.30 
# Pytamy użytkownika, czy pracownik dostaje premię ('Y'/'N'); wyrażenie == 'Y' zwraca True jeśli wpisano 'Y', lub False w innym przypadku
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'
# Sprawdzamy, czy pracownikowi przysługuje premia (czy zmienna is_bonus ma wartość True)
if is_bonus:
    # Jeśli tak, obliczamy pensję całkowitą: pensja podstawowa plus 30% z pensji podstawowej
    total_salary = basic_salary + (basic_salary * bonus)
# W przeciwnym razie (gdy is_bonus to False)
else:
    # Pensja całkowita jest równa samej pensji podstawowej (bez premii)
    total_salary = basic_salary
# Wyświetlamy wysokość pensji podstawowej
print(f'Basic salary: {basic_salary}')
# Wyświetlamy informację, czy premia została uwzględniona (True lub False)
print(f'Bonus included? {is_bonus}')
# Wyświetlamy obliczoną pensję całkowitą
print(f'Total salary: {total_salary}')

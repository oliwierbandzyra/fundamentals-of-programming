###
# Moduł z funkcją sprawdzającą, czy liczba leży w przedziale <x, y>
#
def in_range(number, x, y):
    # zapis x <= number <= y sprawdza oba warunki naraz
    # wynik porównania to od razu True albo False
    return x <= number <= y

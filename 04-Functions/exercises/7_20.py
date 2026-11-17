###
# Zwraca n-tą liczbę pierwszą
#

# Funkcja pomocnicza - sprawdza, czy liczba jest pierwsza
def is_prime(number):
    # liczby mniejsze niż 2 nie są pierwsze
    if number < 2:
        return False
    # szukamy dzielnika od 2 do number - 1
    for divisor in range(2, number):
        if number % divisor == 0:
            # znaleźliśmy dzielnik, więc liczba nie jest pierwsza
            return False
    return True

def f(n):
    found = 0       # ile liczb pierwszych już znaleźliśmy
    candidate = 1   # liczba, którą aktualnie sprawdzamy
    # szukamy dopóki nie znajdziemy n liczb pierwszych
    while found < n:
        candidate = candidate + 1
        if is_prime(candidate):
            found = found + 1
    return candidate

if __name__ == "__main__":
    print('f(1) returns', f(1))
    print('f(5) returns', f(5))

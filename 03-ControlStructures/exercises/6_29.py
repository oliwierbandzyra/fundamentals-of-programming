# Pobieramy od użytkownika liczbę N, czyli ile liczb pierwszych program ma znaleźć
N = int(input("Enter N (number of prime numbers to find): "))
# Tworzymy licznik znalezionych dotąd liczb pierwszych i ustawiamy na 0
primes_found = 0
# Zaczynamy sprawdzanie kandydatów na liczby pierwsze od liczby 2 (najmniejsza liczba pierwsza)
num = 2 
# Wypisujemy nagłówek przed listą liczb (end=" " sprawia, że liczby będą pojawiać się obok w tej samej linii)
print("Prime numbers:", end=" ")
# Pętla while działa dopóki nie znajdziemy N liczb pierwszych
while primes_found < N:
    # Zakładamy wstępnie, że badana liczba num jest liczbą pierwszą (True)
    is_prime = True
    # Pętla for sprawdza wszystkie potencjalne dzielniki i od 2 do num - 1
    for i in range(2, num):
        # Jeśli liczba num dzieli się bez reszty przez i, to nie jest liczbą pierwszą
        if num % i == 0:
            # Zmieniamy flagę is_prime na False
            is_prime = False
            # Przerywamy wewnętrzną pętlę for, bo wystarczy znaleźć jeden dzielnik, by wykluczyć liczbę
            break
    # Jeśli po sprawdzeniu wszystkich dzielników flaga is_prime nadal ma wartość True
    if is_prime:
        # Wypisujemy znalezioną liczbę pierwszą ze spacją
        print(num, end=" ")
        # Zwiększamy licznik znalezionych liczb pierwszych o 1
        primes_found += 1
    # Przechodzimy do sprawdzania kolejnej liczby całkowitej (zwiększamy num o 1)
    num += 1
# Na sam koniec przechodzimy do nowej linii
print()

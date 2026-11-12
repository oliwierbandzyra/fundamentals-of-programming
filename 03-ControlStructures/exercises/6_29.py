N = int(input("Enter N (number of prime numbers to find): "))
primes_found = 0
num = 2 

print("Prime numbers:", end=" ")
while primes_found < N:
    is_prime = True
    # Sprawdzamy, czy 'num' dzieli się bez reszty przez jakąkolwiek liczbę od 2 do num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        primes_found += 1
    num += 1
print()

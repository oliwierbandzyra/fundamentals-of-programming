###
# Silnia obliczana rekurencyjnie (funkcja wywołuje samą siebie)
#
def factorial(n):
    # przypadek bazowy: 0! = 1 i 1! = 1 - tu rekurencja się kończy
    if n == 0 or n == 1:
        return 1
    # n! = n * (n-1)! - funkcja wywołuje samą siebie z mniejszą liczbą
    return n * factorial(n - 1)

if __name__ == "__main__":
    print('5! =', factorial(5))

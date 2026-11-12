# Pobieramy wiek psa w latach ludzkich jako liczbę całkowitą
human_years = int(input("Enter the dog's age in human years: "))
# Sprawdzamy, czy pies ma 2 lata lub mniej
if human_years <= 2:
    # Pierwsze dwa lata życia psa liczymy po 10.5 psiego roku za każdy rok
    dog_years = human_years * 10.5
# W przeciwnym razie (gdy pies ma więcej niż 2 lata)
else:
    # Pierwsze 2 lata to 21 psich lat (2 * 10.5), a każdy kolejny rok powyżej drugiego mnożymy przez 4
    dog_years = 21 + (human_years - 2) * 4
# Wyświetlamy wiek psa w psich latach, zamieniając wynik na liczbę całkowitą za pomocą int()
print(f"The dog's age in dog's years is {int(dog_years)} years.")

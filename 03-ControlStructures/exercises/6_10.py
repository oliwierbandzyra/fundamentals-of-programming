human_years = int(input("Enter the dog's age in human years: "))

# Pierwsze 2 lata życia psa liczymy po 10.5 roku, a każdy kolejny rok powyżej 2 po 4 lata
if human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 21 + (human_years - 2) * 4

print(f"The dog's age in dog's years is {int(dog_years)} years.")

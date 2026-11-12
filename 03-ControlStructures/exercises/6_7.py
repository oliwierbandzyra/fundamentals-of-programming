# Pobieramy wiek użytkownika jako liczbę całkowitą
age = int(input("Enter your age: "))
# Jeśli wiek jest mniejszy niż 13 lat
if age < 13:
    # Wyświetlamy kategorię: Dziecko
    print("Child")
# W przeciwnym razie, jeśli wiek wynosi od 13 do 19 lat włącznie
elif 13 <= age <= 19:
    # Wyświetlamy kategorię: Nastolatek
    print("Teen")
# W przeciwnym razie, jeśli wiek wynosi od 20 do 64 lat włącznie
elif 20 <= age <= 64:
    # Wyświetlamy kategorię: Dorosły
    print("Adult")
# W przeciwnym razie (czyli wiek 65 lat i więcej)
else:
    # Wyświetlamy kategorię: Senior
    print("Senior")

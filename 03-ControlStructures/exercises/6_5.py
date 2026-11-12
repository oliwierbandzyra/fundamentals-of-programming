# Pobieramy od użytkownika temperaturę jako liczbę całkowitą (int)
temperature = int(input("Enter temperature: "))
# Jeśli temperatura jest większa niż 35 stopni
if temperature > 35:
    # Wyświetlamy informację o ekstremalnym upale
    print("It is extremely hot")
# W przeciwnym razie (temperatura <= 35), jeśli jest większa niż 30 stopni
elif temperature > 30:
    # Wyświetlamy informację, że jest gorąco
    print("It is hot")
# W przeciwnym razie (temperatura <= 30), jeśli jest większa lub równa 15 stopni
elif temperature >= 15:
    # Wyświetlamy informację, że jest ciepło
    print("It is warm")
# W przeciwnym razie (temperatura < 15), jeśli jest większa lub równa 0 stopni
elif temperature >= 0:
    # Wyświetlamy informację, że jest zimno
    print("It is cold")
# W każdym innym przypadku (gdy temperatura jest poniżej 0 stopni)
else:
    # Wyświetlamy ostrzeżenie o mrozie
    print("Warning, frost")

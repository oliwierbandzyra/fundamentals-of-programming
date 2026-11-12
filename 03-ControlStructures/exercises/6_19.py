# Wyświetlamy nagłówek ankiety
print("SURVEY")
# Pytanie 1: pobieramy odpowiedź ('y'/'n') i porównujemy z 'y' — wynik True lub False zapisujemy w q1
q1 = input("Are you interested in computer science? (y/n): ") == 'y'
# Pytanie 2: sprawdzamy, czy użytkownik wpisał 'y' i zapisujemy wartość logiczną w q2
q2 = input("Do you like playing computer games? (y/n): ") == 'y'
# Pytanie 3: sprawdzamy, czy użytkownik wpisał 'y' i zapisujemy wartość logiczną w q3
q3 = input("Do you have an Instagram account? (y/n): ") == 'y'
# Wyświetlamy pustą linię (\n) i nagłówek wyników ankiety
print("\nSURVEY RESULTS")
# Wyświetlamy wynik 1. pytania: wyrażenie 'Yes' if q1 else 'No' wstawia 'Yes' gdy q1 to True, a 'No' gdy False
print(f"Interested in computer science: {'Yes' if q1 else 'No'}")
# Wyświetlamy wynik 2. pytania w formie 'Yes' lub 'No'
print(f"Playing computer games: {'Yes' if q2 else 'No'}")
# Wyświetlamy wynik 3. pytania w formie 'Yes' lub 'No'
print(f"Has an Instagram account: {'Yes' if q3 else 'No'}")

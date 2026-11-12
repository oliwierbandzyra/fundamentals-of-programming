print("SURVEY")
# Zapisujemy odpowiedzi od razu jako wartości logiczne True/False
q1 = input("Are you interested in computer science? (y/n): ") == 'y'
q2 = input("Do you like playing computer games? (y/n): ") == 'y'
q3 = input("Do you have an Instagram account? (y/n): ") == 'y'

print("\nSURVEY RESULTS")
# Skrócony zapis warunkowy w f-stringu zamienia True/False na 'Yes'/'No'
print(f"Interested in computer science: {'Yes' if q1 else 'No'}")
print(f"Playing computer games: {'Yes' if q2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if q3 else 'No'}")

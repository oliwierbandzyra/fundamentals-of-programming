# Ustalamy poprawny kod PIN jako tekst "0805"
correct_pin = "0805"
# Ustalamy liczbę dostępnych prób wpisania PIN-u na 3
attempts = 3
# Pętla while działa tak długo, jak liczba pozostałych prób jest większa od 0
while attempts > 0:
    # Prosimy użytkownika o wpisanie kodu PIN
    entered_pin = input("Enter the PIN code: ")
    # Sprawdzamy, czy wpisany PIN jest zgodny z poprawnym
    if entered_pin == correct_pin:
        # Jeśli PIN jest poprawny, wyświetlamy potwierdzenie
        print("PIN correct!")
        # Przerywamy pętlę instrukcją break, bo nie trzeba już podawać PIN-u ponownie
        break
    # W przeciwnym razie (gdy wpisano błędny PIN)
    else:
        # Informujemy o pomyłce
        print("Incorrect...")
        # Zmniejszamy liczbę pozostałych prób o 1
        attempts -= 1
# Po wyjściu z pętli sprawdzamy, czy liczba prób spadła do 0 (co oznacza 3 nieudane próby)
if attempts == 0:
    # Wyświetlamy komunikat o zablokowaniu karty płatniczej
    print("Sorry, your payment card has been blocked.")

# Ustalamy początkowe saldo konta w bankomacie na 1000
balance = 1000
# Ustalamy domyślny kod PIN jako napis '1111'
pin = '1111' 
# Nieskończona pętla while True wyświetla menu bankomatu aż do wybrania opcji wyjścia (6)
while True:
    # Wyświetlamy pustą linię (\n) i nagłówek menu bankomatu
    print("\nATM Menu:")
    # Wyświetlamy opcję 1: sprawdzenie salda
    print("1. Check balance")
    # Wyświetlamy opcję 2: wpłata środków
    print("2. Deposit")
    # Wyświetlamy opcję 3: wypłata środków
    print("3. Withdraw")
    # Wyświetlamy opcję 4: sprawdzenie poprawności PIN-u
    print("4. Check PIN")
    # Wyświetlamy opcję 5: zmiana kodu PIN
    print("5. Change PIN")
    # Wyświetlamy opcję 6: zakończenie pracy programu
    print("6. Exit")
    # Pobieramy wybór użytkownika z klawiatury
    choice = input("Choose an option: ")
    # Jeśli użytkownik wybrał '1'
    if choice == '1':
        # Wyświetlamy aktualny stan konta
        print(f"Your balance is: {balance}")
    # W przeciwnym razie, jeśli wybrał '2' (wpłata)
    elif choice == '2':
        # Pobieramy kwotę wpłaty jako liczbę zmiennoprzecinkową (float, np. z groszami)
        amount = float(input("Enter amount to deposit: "))
        # Powiększamy saldo o wpłaconą kwotę
        balance += amount
    # W przeciwnym razie, jeśli wybrał '3' (wypłata)
    elif choice == '3':
        # Pobieramy kwotę do wypłaty jako liczbę zmiennoprzecinkową (float)
        amount = float(input("Enter amount to withdraw: "))
        # Sprawdzamy, czy na koncie jest wystarczająco dużo pieniędzy
        if amount <= balance:
            # Jeśli tak, odejmujemy wypłacaną kwotę od salda
            balance -= amount
        # W przeciwnym razie (brak środków)
        else:
            # Wyświetlamy komunikat o niewystarczających środkach
            print("Insufficient funds!")
    # W przeciwnym razie, jeśli wybrał '4' (sprawdzenie PIN)
    elif choice == '4':
        # Prosimy o wpisanie PIN-u do weryfikacji
        entered_pin = input("Enter your PIN to check: ")
        # Sprawdzamy, czy wpisany PIN zgadza się z zapisanym w zmiennej pin
        if entered_pin == pin:
            # Informujemy, że PIN jest prawidłowy
            print("PIN is correct.")
        else:
            # Informujemy, że PIN jest błędny
            print("Incorrect PIN.")
    # W przeciwnym razie, jeśli wybrał '5' (zmiana PIN)
    elif choice == '5':
        # Pobieramy nowy PIN od użytkownika
        new_pin = input("Enter new 4-digit PIN: ")
        # Sprawdzamy dwa warunki: czy długość (len) wynosi dokładnie 4 ORAZ czy składa się wyłącznie z cyfr (isdigit)
        if len(new_pin) == 4 and new_pin.isdigit():
            # Zapisujemy nowy PIN w zmiennej pin
            pin = new_pin
            # Potwierdzamy zmianę PIN-u
            print("PIN changed successfully.")
        else:
            # Informujemy o błędnym formacie nowego PIN-u
            print("Invalid PIN format. Must be exactly 4 digits.")
    # W przeciwnym razie, jeśli wybrał '6' (wyjście)
    elif choice == '6':
        # Wyświetlamy pożegnanie
        print("Goodbye!")
        # Przerywamy nieskończoną pętlę while True, co kończy działanie programu
        break
    # Jeśli użytkownik wpisał cokolwiek innego niż cyfry 1-6
    else:
        # Informujemy o nieprawidłowej opcji
        print("Invalid option.")

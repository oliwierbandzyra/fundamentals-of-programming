balance = 1000
pin = '1111' 
# menu bankomatu chodzi w petli az wybierzesz 6
while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        print(f"Your balance is: {balance}")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        # sprawdza czy nie chcesz wyplacic wiecej niz masz
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds!")
    elif choice == '4':
        entered_pin = input("Enter your PIN to check: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("Incorrect PIN.")
    elif choice == '5':
        new_pin = input("Enter new 4-digit PIN: ")
        # musi miec dokladnie 4 znaki i same cyfry
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid PIN format. Must be exactly 4 digits.")
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

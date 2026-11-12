correct_pin = "0805"
attempts = 3

# Użytkownik ma maksymalnie 3 próby na wpisanie poprawnego kodu PIN
while attempts > 0:
    entered_pin = input("Enter the PIN code: ")
    if entered_pin == correct_pin:
        print("PIN correct!")
        break
    else:
        print("Incorrect...")
        attempts -= 1

if attempts == 0:
    print("Sorry, your payment card has been blocked.")

###
# Credit card payment 
#

account_balance = 500

# Wczytanie kwoty całkowitej do zapłaty
total_payment = int(input('Enter total payment: '))

# Jeżeli płatność jest mniejsza bądź równa saldu, transakcja przechodzi
if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds') # W przeciwnym razie brak środków
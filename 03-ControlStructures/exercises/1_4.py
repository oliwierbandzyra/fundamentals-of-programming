account_balance = 500
total_payment = int(input('Enter total payment: '))

# Płatność przejdzie tylko wtedy, gdy kwota nie przekracza dostępnego salda
if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')

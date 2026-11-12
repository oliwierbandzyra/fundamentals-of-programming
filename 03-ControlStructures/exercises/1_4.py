# Ustalamy początkowy stan konta równy 500 i zapisujemy w zmiennej account_balance
account_balance = 500
# Pobieramy od użytkownika kwotę do zapłaty, zamieniamy na liczbę całkowitą (int) i zapisujemy w zmiennej total_payment
total_payment = int(input('Enter total payment: '))
# Sprawdzamy, czy kwota do zapłaty jest mniejsza lub równa (<=) stanowi konta
if total_payment <= account_balance:
    # Jeśli środków wystarczy, wyświetlamy komunikat o zrealizowaniu płatności
    print('Payment completed')
# W przeciwnym razie (else), czyli gdy kwota do zapłaty jest większa niż stan konta
else:
    # Wyświetlamy komunikat o braku wystarczających środków
    print('No funds')

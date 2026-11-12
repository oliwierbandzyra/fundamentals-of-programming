# Pobieramy od użytkownika numer miesiąca (od 1 do 12) jako liczbę całkowitą
month = int(input('Enter month number (1..12): '))
# Sprawdzamy, czy miesiąc to styczeń (1), marzec (3), maj (5), lipiec (7), sierpień (8), październik (10) lub grudzień (12)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    # Wszystkie te miesiące mają 31 dni
    days = 31 
# W przeciwnym razie sprawdzamy, czy miesiąc to kwiecień (4), czerwiec (6), wrzesień (9) lub listopad (11)
elif month == 4 or month == 6 or month == 9 or month == 11:
    # Te miesiące mają 30 dni
    days = 30
# W przeciwnym razie (pozostaje tylko luty, czyli miesiąc 2)
else:
    # Zakładamy rok nieprzestępny, więc luty ma 28 dni
    days = 28
# Wyświetlamy, ile dni ma podany miesiąc
print(f'Month {month} has {days} days')

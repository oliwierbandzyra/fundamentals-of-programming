# Zapisujemy całkowitą liczbę zadań w teście (20) w zmiennej total_tasks
total_tasks = 20
# Pobieramy od użytkownika liczbę poprawnie rozwiązanych zadań jako liczbę całkowitą (int)
tasks_ok = int(input('Enter number of correctly completed tasks: '))
# Tworzymy zmienną logiczną test_passed i na początku ustawiamy ją na False (fałsz - test niezdany)
test_passed = False
# Sprawdzamy, czy liczba poprawnych zadań wynosi co najmniej (>=) 50% (czyli 0.5) wszystkich zadań
if tasks_ok >= total_tasks * 0.5:
    # Jeśli warunek jest spełniony, zmieniamy wartość zmiennej test_passed na True (prawda - test zdany)
    test_passed = True
# Sprawdzamy, czy zmienna test_passed ma wartość True
if test_passed:
    # Jeśli test jest zdany, wyświetlamy gratulacje
    print('Congratulations! You passed the test.')
# W przeciwnym razie (gdy test_passed to False)
else:
    # Wyświetlamy komunikat o niezdaniu testu
    print('Unfortunately, you failed the test.')

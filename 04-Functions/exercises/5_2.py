# import converters - dołączamy nasz moduł (plik converters.py w tym samym folderze)
# Funkcje wywołujemy jako converters.nazwa_funkcji()
import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm') # wywołanie funkcji m_to_cm z modułu converters
print(f'Two hundred cm is {converters.cm_to_m(200)}m') # wywołanie funkcji cm_to_m z modułu converters
# nowe funkcje
print(f'Two hundred cm is {converters.cm_to_inches(200)} inches') # wywołanie funkcji cm_to_inches z modułu converters
print(f'5 feet 9 inches is {converters.feet_inches_to_cm(5, 9)}cm') # wywołanie funkcji feet_inches_to_cm z modułu converters

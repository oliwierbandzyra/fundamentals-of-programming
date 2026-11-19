###
# Sprawdza, czy nawiasy () {} [] w wyrażeniu są poprawnie użyte (stos)
#
import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # nawiasy poprawne
expression2 = "[(2+3]/4)"                 # nawiasy niepoprawne
expression3 = "(2-3*4+(5/6)"              # nawiasy niepoprawne

# Funkcja zwraca True, jeśli nawiasy w wyrażeniu są poprawne, w przeciwnym razie False
def brackets_ok(expression):
    # słownik: do każdego nawiasu zamykającego przypisany jest jego nawias otwierający
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = queue.LifoQueue()

    for char in expression:
        if char in '([{':
            # nawias otwierający odkładamy na stos
            stack.put(char)
        elif char in ')]}':
            # nawias zamykający: jeśli stos jest pusty, nie ma do niego pary
            if stack.empty():
                return False
            # zdejmujemy ze stosu ostatni otwarty nawias i sprawdzamy, czy pasuje
            opening = stack.get()
            if opening != pairs[char]:
                return False
        # wszystkie pozostałe znaki (cyfry, działania) pomijamy

    # na końcu stos musi być pusty - inaczej któryś nawias nie został zamknięty
    return stack.empty()

if brackets_ok(expression1):
    print(expression1, '- brackets ok')
else:
    print(expression1, '- brackets not correct')

if brackets_ok(expression2):
    print(expression2, '- brackets ok')
else:
    print(expression2, '- brackets not correct')

if brackets_ok(expression3):
    print(expression3, '- brackets ok')
else:
    print(expression3, '- brackets not correct')

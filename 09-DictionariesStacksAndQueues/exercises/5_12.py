###
# Odwraca tekst za pomocą stosu
#
import queue

# Funkcja zwraca odwrócony tekst
def reverse_text(text):
    stack = queue.LifoQueue()
    # każdy znak tekstu odkładamy na stos
    for char in text:
        stack.put(char)
    # ze stosu zdejmujemy znaki od ostatniego do pierwszego
    reversed_text = ''
    while not stack.empty():
        reversed_text = reversed_text + stack.get()
    return reversed_text

text = input('Enter any text: ')
print('Reversed text:', reverse_text(text))

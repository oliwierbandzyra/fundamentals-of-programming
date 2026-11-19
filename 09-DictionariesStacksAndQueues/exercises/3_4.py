###
# Zamienia liczbę naturalną na liczbę binarną (stos)
#
import queue

stack = queue.LifoQueue()

number = int(input('Natural number: '))

# Dzielimy liczbę przez 2, a resztę z dzielenia odkładamy na stos.
# Powtarzamy, aż liczba dojdzie do 0.
# Dla 0 pętla się nie wykona, więc ten przypadek obsługujemy osobno.
if number == 0:
    stack.put(0)

while number > 0:
    remainder = number % 2   # % to reszta z dzielenia
    stack.put(remainder)
    number = number // 2     # // to dzielenie całkowite

# Zdejmujemy wszystkie reszty ze stosu. Wychodzą od ostatniej do pierwszej,
# a właśnie w takiej kolejności tworzą liczbę binarną.
binary = ''
while not stack.empty():
    binary = binary + str(stack.get())

print('Binary number:', binary)

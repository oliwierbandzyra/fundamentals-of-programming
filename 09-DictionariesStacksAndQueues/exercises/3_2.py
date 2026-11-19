###
# Symulacja przycisku "Wstecz" w przeglądarce internetowej (stos)
#
import queue

# LifoQueue to stos: ostatni dodany element jest pobierany jako pierwszy
visited_websites = queue.LifoQueue()

# kilka wcześniej odwiedzonych stron
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

# strona, którą użytkownik ogląda w tej chwili (na początku jeszcze żadna)
current = ''

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        # jeśli stos jest pusty, nie ma już dokąd wracać - kończymy program
        if visited_websites.empty():
            break
        else:
            print('<-- Going back to a previously visited website')
            # get() zdejmuje ze stosu ostatnio odwiedzoną stronę
            current = visited_websites.get()
    elif website != "":
        # wchodzimy na nową stronę: poprzednią stronę odkładamy na stos,
        # żeby można było do niej wrócić przyciskiem "wstecz"
        if current != '':
            visited_websites.put(current)
        current = website

    # wypisanie nazwy strony, którą aktualnie oglądamy
    print('You are currently viewing:', current)
    print()

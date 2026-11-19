###
# Liczy, ile razy każde słowo występuje w akapicie
#
paragraph = "cat dog mouse cat rat cat mouse"

# pusty słownik: kluczem będzie słowo, wartością liczba jego wystąpień
counts = {}

# split() dzieli tekst na pojedyncze słowa (lista)
for word in paragraph.split():
    if word in counts:
        # słowo już było - zwiększamy jego licznik o 1
        counts[word] += 1
    else:
        # słowo pojawia się pierwszy raz - zaczynamy liczyć od 1
        counts[word] = 1

for word, count in counts.items():
    print(word, ':', count)

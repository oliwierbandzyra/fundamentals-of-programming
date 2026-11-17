###
# Funkcja zwraca godzinę jako tekst w formacie 24-godzinnym lub 12-godzinnym
#
def time_string(hours, minutes, time_format):
    if time_format == '24':
        # :02d oznacza liczbę zawsze dwucyfrową, z zerem z przodu (np. 08, 05)
        result = f'{hours:02d}:{minutes:02d}'
    else:
        # w formacie 12h do godziny 11:59 jest am, od 12:00 jest pm
        if hours < 12:
            suffix = 'am'
        else:
            suffix = 'pm'
        # reszta z dzielenia przez 12 zamienia 13 na 1, 19 na 7 itd.
        hours_12 = hours % 12
        # północ i południe to godzina 12, a nie 0
        if hours_12 == 0:
            hours_12 = 12
        # godzina bez zera z przodu, minuty zawsze dwucyfrowe
        result = f'{hours_12}:{minutes:02d}{suffix}'
    return result

# Program testujący - wypisujemy wynik funkcji dla wszystkich przykładów
print(time_string(15, 38, '24'))   # 15:38
print(time_string(8, 3, '24'))     # 08:03
print(time_string(0, 5, '24'))     # 00:05
print(time_string(11, 15, '12'))   # 11:15am
print(time_string(0, 7, '12'))     # 12:07am
print(time_string(7, 30, '12'))    # 7:30am
print(time_string(12, 46, '12'))   # 12:46pm
print(time_string(13, 10, '12'))   # 1:10pm
print(time_string(19, 2, '12'))    # 7:02pm

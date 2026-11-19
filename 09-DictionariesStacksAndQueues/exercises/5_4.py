###
# Oblicza łączną liczbę godzin zajęć w semestrze zimowym
#
winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

total_hours = 0
# values() zwraca same wartości (liczby godzin), bez kluczy
for hours in winter_semester.values():
    total_hours += hours

print('The total number of hours in the winter semester is', total_hours)

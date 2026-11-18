###
# Zwraca nazwę dnia tygodnia dla podanego numeru dnia (1-Monday ... 7-Sunday)
#
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    # numer dnia zaczyna się od 1, a indeks listy od 0, dlatego n - 1
    return weekdays[n - 1]

print('Day 1 is', weekday(1))
print('Day 4 is', weekday(4))
print('Day 7 is', weekday(7))

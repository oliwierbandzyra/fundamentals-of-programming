###
# Łączy dwa słowniki z danymi osobowymi w jeden słownik person
#
basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# update() dopisuje do słownika wszystkie pary klucz-wartość z innego słownika
person = {}
person.update(basic_data)
person.update(advanced_data)

# w słowniku person jest teraz 5 par klucz-wartość
for key, value in person.items():
    print(f"{key} : {value}")

###
# Operacje na słowniku z danymi osoby
#

# Rodzaje wartości w tym słowniku:
# "name" - tekst (str), "surname" - tekst (str), "age" - liczba całkowita (int),
# "hobby" - lista (list), "married" - wartość logiczna (bool),
# "phone" - drugi słownik (dict), czyli słownik w słowniku
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# 1. Wyświetlenie imienia - odczyt wartości po kluczu
print("Name:", person["name"])

# 2. Wyświetlenie hobby (to jest lista)
print("Hobby:", person["hobby"])

# 3. Wyświetlenie całego słownika
print("Person:", person)

# 4. Zmiana nazwiska - przypisanie nowej wartości do istniejącego klucza
person["surname"] = "Nowak"

# 5. Zmiana stanu cywilnego: not zamienia True na False (i odwrotnie)
person["married"] = not person["married"]

# 6. Dodanie płci - nowy klucz, więc para zostanie dodana do słownika
person["gender"] = "male"

# 7. Dodanie hobby - person["hobby"] to lista, więc używamy append()
person["hobby"].append("bicycle")

# 8. Dodanie telefonu służbowego - person["phone"] to słownik, więc dodajemy nowy klucz
person["phone"]["work"] = "313131444"

# 9. Wyświetlenie całej zawartości słownika (pętla po kluczach i wartościach)
print()
for key, value in person.items():
    print(f"{key} : {value}")

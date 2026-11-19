###
# Tablica (lista) słowników - kraje i liczba ich mieszkańców
#

# Lista zawiera 5 słowników, każdy słownik to jeden kraj
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83200000},
    {"name": "France", "population": 67800000},
    {"name": "Italy", "population": 59000000},
    {"name": "Spain", "population": 47400000}
]

print("COUNTRY  POPULATION")
# pętla bierze po kolei każdy słownik (kraj) z listy
for country in countries:
    # :<9 oznacza, że nazwa zajmuje 9 znaków, dzięki temu liczby są równo pod sobą
    print(f"{country['name']:<9}{country['population']}")

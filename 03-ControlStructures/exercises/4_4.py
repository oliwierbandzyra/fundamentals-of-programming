# Zapisujemy nazwę uczelni w zmiennej tekstowej university
university = 'Krakow University of Economics'
# Tworzymy pusty napis (string) w zmiennej university_expanded, do którego będziemy doklejać litery ze spacjami
university_expanded = ''
# Pętla for bierze po kolei każdy znak ze zmiennej university
for char in university:
    # Do dotychczasowego tekstu doklejamy aktualny znak oraz jedną spację
    university_expanded = university_expanded + char + ' '
# Wyświetlamy oryginalny tekst
print(university) 
# Wyświetlamy tekst rozstrzelony (z dodaną spacją po każdym znaku)
print(university_expanded)

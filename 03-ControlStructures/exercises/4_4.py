university = 'Krakow University of Economics'
university_expanded = ''

# Budujemy nowy napis, doklejając po każdym znaku dodatkową spację
for char in university:
    university_expanded = university_expanded + char + ' '

print(university) 
print(university_expanded)

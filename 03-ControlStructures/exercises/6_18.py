# Pobieramy współrzędną x punktu jako liczbę całkowitą
x = int(input("x = "))
# Pobieramy współrzędną y punktu jako liczbę całkowitą
y = int(input("y = "))
# Jeśli obie współrzędne (x i y) są dodatnie
if x > 0 and y > 0:
    # Punkt leży w pierwszej ćwiartce układu współrzędnych
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
# W przeciwnym razie, jeśli x jest ujemne, a y dodatnie
elif x < 0 and y > 0:
    # Punkt leży w drugiej ćwiartce układu współrzędnych
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
# W przeciwnym razie, jeśli obie współrzędne (x i y) są ujemne
elif x < 0 and y < 0:
    # Punkt leży w trzeciej ćwiartce układu współrzędnych
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
# W przeciwnym razie, jeśli x jest dodatnie, a y ujemne
elif x > 0 and y < 0:
    # Punkt leży w czwartej ćwiartce układu współrzędnych
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
# W przeciwnym razie, jeśli x wynosi 0, a y jest różne od 0
elif x == 0 and y != 0:
    # Punkt leży dokładnie na osi pionowej Y
    print(f"Point P({x},{y}) is on the Y axis")
# W przeciwnym razie, jeśli y wynosi 0, a x jest różne od 0
elif y == 0 and x != 0:
    # Punkt leży dokładnie na osi poziomej X
    print(f"Point P({x},{y}) is on the X axis")
# W każdym innym przypadku (gdy zarówno x == 0, jak i y == 0)
else:
    # Punkt znajduje się w samym środku układu współrzędnych, czyli w punkcie (0,0)
    print(f"Point P({x},{y}) is in the position (0,0)")

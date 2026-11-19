###
# Znajduje nieobecnych studentów
#
all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

# Różnica zbiorów (-): elementy, które są w pierwszym zbiorze, a nie ma ich w drugim
absent_students = all_students - attended_students
print(absent_students)

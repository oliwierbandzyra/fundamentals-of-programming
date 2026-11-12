age = int(input("Enter your age: "))

# Przypisujemy grupę wiekową na podstawie podanego wieku
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
elif 20 <= age <= 64:
    print("Adult")
else:
    print("Senior")

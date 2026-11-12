total_sum = 0
count = 0

# Pętla działa w nieskończoność, dopóki użytkownik nie wpisze 0 (wtedy 'break' ją przerywa)
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number
    count += 1

print(f"The total sum of the numbers is: {total_sum}")

# Zabezpieczenie przed dzieleniem przez zero, gdyby ktoś od razu wpisał 0
if count > 0:
    mean = total_sum / count
    print(f"Arithmetic mean: {mean}")

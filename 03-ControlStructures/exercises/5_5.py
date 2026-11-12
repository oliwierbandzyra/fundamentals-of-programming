total_sum = 0
count = 0
# nieskonczona petla, przerywa dopiero po wpisaniu 0 (break)
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number
    count += 1
print(f"The total sum of the numbers is: {total_sum}")
# zeby nie dzielic przez 0 jak ktos od razu da 0
if count > 0:
    mean = total_sum / count
    print(f"Arithmetic mean: {mean}")

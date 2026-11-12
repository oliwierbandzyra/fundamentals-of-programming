month = int(input('Enter month number (1..12): '))
# sprawdzam od konca roku zeby nie pisac przedzialow
if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
elif month >= 1:
    quarter = 1
print(f'Month {month} is in quarter {quarter}')

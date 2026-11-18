###
# Oblicza wydatki miesięczne w podziale na kategorie i tygodnie
#
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# sumy dla kategorii (kolumn) i tygodni (wierszy)
category_totals = [0, 0, 0]
week_totals = [0, 0, 0, 0]
total = 0

# i to numer tygodnia (wiersza), j to numer kategorii (kolumny)
for i in range(len(monthly_expenses)):
    for j in range(len(monthly_expenses[i])):
        value = monthly_expenses[i][j]
        category_totals[j] = category_totals[j] + value
        week_totals[i] = week_totals[i] + value
        total = total + value

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total)

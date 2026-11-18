###
# Raport ze stacji pogodowej
#
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# liczba pomiarów
measurements = len(temperatures)

# średnia temperatura: suma wszystkich pomiarów podzielona przez ich liczbę
temp_total = 0
for temp in temperatures:
    temp_total = temp_total + temp
avg_temp = round(temp_total / measurements, 2)

# najniższa i najwyższa temperatura (wbudowane funkcje min i max)
min_temp = min(temperatures)
max_temp = max(temperatures)

# liczba dni z temperaturą poniżej zera (pętla while)
negative_temp = 0
i = 0
while i < len(temperatures):
    if temperatures[i] < 0:
        negative_temp = negative_temp + 1
    i = i + 1

print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:', measurements)
print('Average temperature in the month:', avg_temp)
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)

###
# Informacje o miejscach w kinie
#
# 5x5 miejsc w kinie: A = Available (wolne), B = Booked (zajęte)
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

# Liczba wszystkich miejsc (każde pole tablicy to jedno miejsce)
def seats_total(seats):
    counter = 0
    for row in seats:
        for seat in row:
            counter = counter + 1
    return counter

# Liczba wolnych miejsc
def seats_available(seats):
    counter = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                counter = counter + 1
    return counter

# Liczba zajętych miejsc
def seats_booked(seats):
    counter = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                counter = counter + 1
    return counter

# Status miejsca w danym rzędzie i miejscu (numerujemy od 1, a indeksy od 0)
def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == 'A':
        return 'available'
    else:
        return 'booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))

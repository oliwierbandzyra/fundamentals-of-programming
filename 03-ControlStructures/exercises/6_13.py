car_speed = int(input("Enter car speed: "))
speed_limit_min = 40
speed_limit_max = 140

# Ostrzegamy, jeśli prędkość jest poniżej minimum lub powyżej maksimum
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")

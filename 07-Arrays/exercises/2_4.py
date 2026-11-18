###
# Wypisuje tygodniowy plan posiłków z nazwami dni
#
# Plan posiłków [Breakfast, Lunch, Dinner] na 7 dni
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Zwraca nazwę dnia tygodnia
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

# Zwraca tekst z posiłkami danego dnia, oddzielonymi przecinkami
def day_meal_plan(meal_plan, day_number):
    # meal_plan[day_number - 1] to wiersz (lista) z posiłkami tego dnia
    meals = meal_plan[day_number - 1]
    result = ''
    for i in range(len(meals)):
        # przecinek dajemy przed każdym posiłkiem oprócz pierwszego
        if i > 0:
            result = result + ', '
        result = result + meals[i]
    return result

# Wypisuje plan na cały tydzień
print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')
for day in range(1, 8):
    print(weekday(day) + ': ' + day_meal_plan(meal_plan, day))

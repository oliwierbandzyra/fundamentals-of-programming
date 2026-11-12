# Tworzymy zmienną na całkowity czas prania i ustawiamy ją na 0
total_washing_time = 0
# Pobieramy od użytkownika symbol wybranego programu prania ('j', 'u' lub 's')
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
# Pytamy, czy dodać dodatkowe płukanie ('y' lub 'n')
extra_rinse = input('Extra rinse? (y/n): ')
# Pytamy, czy dodać dodatkowe wirowanie ('y' lub 'n')
extra_spin = input('Extra spin? (y/n): ')
# Jeśli wybrano program 'j' (kurtka)
if program == 'j':
    # Dodajemy 40 minut do czasu prania
    total_washing_time += 40
# W przeciwnym razie, jeśli wybrano program 'u' (bielizna)
elif program == 'u':
    # Dodajemy 70 minut do czasu prania
    total_washing_time += 70
# W przeciwnym razie, jeśli wybrano program 's' (buty)
elif program == 's':
    # Dodajemy 20 minut do czasu prania
    total_washing_time += 20
# Sprawdzamy niezależnie, czy użytkownik wybrał dodatkowe płukanie ('y')
if extra_rinse == 'y':
    # Jeśli tak, doliczamy 15 minut
    total_washing_time += 15
# Sprawdzamy niezależnie, czy użytkownik wybrał dodatkowe wirowanie ('y')
if extra_spin == 'y':
    # Jeśli tak, doliczamy 9 minut
    total_washing_time += 9
# Wyświetlamy całkowity czas trwania prania w minutach
print(f"Total washing time: {total_washing_time} minutes")

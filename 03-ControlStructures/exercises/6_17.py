# Pobieramy godzinę w formacie 24-godzinnym jako tekst (np. '14:30')
time_24 = input("Enter time (24-hour format): ")
# Metoda split(":") dzieli tekst w miejscu dwukropka na dwie części: godziny oraz minuty
hours, minutes = time_24.split(":")
# Zamieniamy godziny z tekstu na liczbę całkowitą (int), aby móc wykonywać na nich obliczenia
hours = int(hours)
# Domyślnie ustawiamy oznaczenie pory dnia na "am" (przed południem)
am_pm = "am"
# Jeśli godzina wynosi 12 lub więcej (czyli jest południe lub popołudnie/wieczór)
if hours >= 12:
    # Zmieniamy oznaczenie pory dnia na "pm"
    am_pm = "pm"
    # Jeśli godzina jest większa niż 12 (np. 13, 14... 23)
    if hours > 12:
        # Odejmujemy 12, aby uzyskać format 12-godzinny (np. 14 - 12 = 2)
        hours -= 12
# W przeciwnym razie, jeśli godzina to 0 (północ w formacie 24h)
elif hours == 0:
    # W formacie 12-godzinnym północ zapisujemy jako 12 (am)
    hours = 12
# Wyświetlamy skonwertowany czas w formacie 12-godzinnym
print(f"Time in 12-hour format: {hours}:{minutes}{am_pm}")

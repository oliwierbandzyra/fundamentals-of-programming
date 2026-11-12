time_24 = input("Enter time (24-hour format): ")
hours, minutes = time_24.split(":")
hours = int(hours)
am_pm = "am"
if hours >= 12:
    am_pm = "pm"
    if hours > 12:
        hours -= 12
elif hours == 0:
    hours = 12
print(f"Time in 12-hour format: {hours}:{minutes}{am_pm}")
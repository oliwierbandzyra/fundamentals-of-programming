import time

t = int(input("Enter time in seconds: "))

# Odliczamy w dół co sekundę; ostatnie 5 sekund wypisujemy słownie
while t > 0:
    if t == 5:
        print("five")
    elif t == 4:
        print("four")
    elif t == 3:
        print("three")
    elif t == 2:
        print("two")
    elif t == 1:
        print("one")
    else:
        print(t)
    t -= 1
    time.sleep(1)  # pauza na 1 sekundę w czasie rzeczywistym

print("Time is up!")

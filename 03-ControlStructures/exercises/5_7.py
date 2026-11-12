import time
t = int(input("Enter time in seconds: "))
# odlicza co sekunde, ostatnie 5 wypisuje slownie
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
    time.sleep(1)
print("Time is up!")

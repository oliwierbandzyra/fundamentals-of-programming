import random

# '_' używamy jako nazwy zmiennej w pętli, gdy interesuje nas tylko liczba powtórzeń (20 razy)
for _ in range(20): 
    print(random.randint(5, 10), end=" ")

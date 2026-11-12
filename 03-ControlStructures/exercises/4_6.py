# Tworzymy zmienną sum (suma) i ustawiamy jej wartość początkową na 0
sum = 0
# Pętla for generuje kolejne liczby całkowite od 5 do 10 włącznie (range(5, 11) zatrzymuje się przed 11)
for i in range(5, 11):
    # Dodajemy aktualną liczbę i do zmiennej sum (skrót od: sum = sum + i)
    sum += i 
# Po zakończeniu pętli wyświetlamy ostateczną sumę liczb
print(f'Sum is {sum}')

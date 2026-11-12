sum = 0

for i in range(1, 11):
    # Jeśli liczba jest nieparzysta, 'continue' przeskakuje od razu do kolejnego obrotu pętli
    if not i % 2 == 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')

N = 10
sum_even = 0
i = 1
# sumuje parzyste od 1 do N
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1 
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

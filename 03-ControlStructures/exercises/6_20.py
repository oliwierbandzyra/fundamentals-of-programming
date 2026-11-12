num = int(input("Enter decimal number: "))
original_num = num
binary = ""
if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2 
print(f"{original_num}(10) = {binary}(2)")
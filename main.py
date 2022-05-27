numbers = [5, 2, 23, 15, 30, 26, 20, 40, 14]
large_num = 0

for num in numbers:
    if num > large_num:
        large_num = num
print("The largest number is " + str(large_num))

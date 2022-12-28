numbers = input().split()
total_numbers_counter = 0
for num in range(int(numbers[0]), int(numbers[1]) + 1):
    zero_counter = 0
    counter = 0
    for digit in str(num):
        if digit == '0':
            zero_counter += 1
        elif digit != '0':
            if num % int(digit) == 0:
                counter += 1
    if counter + zero_counter == len(str(num)):
        total_numbers_counter += 1
print(total_numbers_counter)

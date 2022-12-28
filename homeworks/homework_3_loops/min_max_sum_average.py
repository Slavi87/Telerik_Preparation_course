import sys
number = int(input())
sum_numbers = 0
min_num = sys.maxsize
max_num = -sys.maxsize
for i in range(1, number + 1):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
average_num = sum_numbers / number        
print(f'min = {min_num}')
print(f'max = {max_num}')
print(f'sum = {sum_numbers}')
print(f'avg = {round(average_num, 2)}')



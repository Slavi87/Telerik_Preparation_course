array = [int(el) for el in input().split()]
sum_nums = 0
for el in array:
    if el % 3 == 0 and el % 7 == 0:
        sum_nums += el
str_num = str(sum_nums)
str_sum = 0
for i in str_num:
    str_sum += int(i)
print(str_sum)
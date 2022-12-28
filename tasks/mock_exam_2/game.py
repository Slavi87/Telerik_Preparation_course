number = list(input())
first_num = 0
second_num = 0
third_num = 0
for i in number:
    first_num = int(number[0])
    second_num = int(number[1])
    third_num = int(number[2])
total_sum = first_num + second_num + third_num
total_multiply = first_num * second_num * third_num
first_combination = first_num + second_num * third_num
second_combination = first_num * second_num + third_num
max_num = max(total_multiply, total_sum, first_combination, second_combination)
print(max_num)


# POINTS = 100


n = int(input())
numbers = [0] * 10
max_counter = 0
indices = []
for i in range(n):
    num = int(input())
    numbers[num - 1] += 1

for el in range(len(numbers)):
    if numbers[el] == max(numbers):
        indices.append(el + 1)
print(min(indices))


# POINTS = 100



# n = int(input())
# digits = [0] * 10
# max_count = 0
# max_index = 0
# for i in range(n):
#     num = int(input())
#     digits[num-1] += 1
#     if digits[num-1] > max_count or digits[num-1] == max_count and num - 1 < max_index:
#         max_count = digits[num - 1]
#         max_index = num - 1
# print(max_index + 1)

# POINTS = 100


# 2
# n = int(input())
# numbers = [int(input()) for i in range(n)]
# max_counter = 0
# digits = []
# for digit in numbers:
#     digit_counter = numbers.count(digit)
#     while digit in numbers:
#         numbers.remove(digit)
#     if digit_counter == max_counter:
#         digits.append(digit)
#     elif digit_counter > max_counter:
#         max_counter = digit_counter
#         digits.clear()
#         digits.append(digit)
# print(min(digits))

# POINTS = 40



# 3
# n = int(input())
# numbers = []
# repeated_numbers = []
# max_counter = 0
# final_lst = []
# for i in range(n):
#     number = int(input())
#     if number not in numbers:
#         numbers.append(number)
#     else:
#         repeated_numbers.append(number)
# for el in repeated_numbers:
#     counter = repeated_numbers.count(el)
#     while el in repeated_numbers:
#         repeated_numbers.remove(el)
#     if counter > max_counter:
#         max_counter = counter
#         final_lst.clear()
#         final_lst.append(el)
#     elif counter == max_counter:
#         final_lst.append(el)
#     else:
#         final_lst = final_lst
# if len(final_lst) > 1:
#     print(min(final_lst))
# elif len(final_lst) == 0:
#     print(*numbers)
# elif len(final_lst) == 1:
#     print(*final_lst)
# POINTS = 40



number = list(input())
num_lst = []
for el in number:
    if el.isdigit():
        num_lst.append(int(el))
sum_nums = sum(num_lst) % 9
if sum_nums == 0:
    sum_nums = 9
print(sum_nums)



# POINTS = 90
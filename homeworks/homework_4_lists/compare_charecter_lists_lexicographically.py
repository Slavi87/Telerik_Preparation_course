first_lst = input().split(',')
second_lst = input().split(',')
sum_first_lst = 0
sum_second_lst = 0
for el in first_lst:
    sum_first_lst += ord(el)
for i in second_lst:
    sum_second_lst += ord(i)
if sum_second_lst > sum_first_lst:
    print('First')
elif sum_second_lst < sum_first_lst:
    print('Second')
else:
    print('Equal')

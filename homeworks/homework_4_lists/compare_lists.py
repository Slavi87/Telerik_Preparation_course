n = int(input())
first_lst = []
second_lst = []
while len(first_lst) < n:
    number = int(input())
    first_lst.append(number)
while len(second_lst) < n:
    number = int(input())
    second_lst.append(number)
if first_lst == second_lst:
    print('Equal')
else:
    print('Not equal')



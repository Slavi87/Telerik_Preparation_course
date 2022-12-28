n = int(input())
num_lst = []
num = ''
max_counter = 0
for i in range(n):
    number = int(input())
    num_lst.append(number)
for el in num_lst:
    counter = num_lst.count(el)
    if counter > max_counter:
        max_counter = counter
        num = str(el)
print(f'{num}({max_counter} times)')
numbers = [el for el in input().split()]
searched_num = []
num = ''
for el in numbers:
    if el in searched_num:
        num = el
    else:
        searched_num.append(el)
print(num)
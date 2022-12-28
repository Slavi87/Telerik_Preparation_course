lst = [el for el in input().split(',')]
new_lst = []
for el in lst:
    if el in new_lst:
        continue
    else:
        new_lst.append(el)
print(*new_lst, sep=',')
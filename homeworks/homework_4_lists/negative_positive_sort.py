numbers = [int(el) for el in input().split()]
negative_lst = []
positive_lst = []
for el in numbers:
    if el < 0:
        negative_lst.append(str(el))
    elif el > 0:
        positive_lst.append(str(el))
    else:
        continue
final_lst = negative_lst + positive_lst
print(' '.join(final_lst))
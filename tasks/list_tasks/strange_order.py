lst_numbers = [int(el) for el in input().split(',')]
positive_numbers = []
negative_numbers = []
zeros = []
for el in lst_numbers:
    if el > 0:
        positive_numbers.append(el)
    elif el < 0:
        negative_numbers.append(el)
    else:
        zeros.append(el)
final_lst = list(negative_numbers + zeros + positive_numbers)
print(*final_lst, sep=',')
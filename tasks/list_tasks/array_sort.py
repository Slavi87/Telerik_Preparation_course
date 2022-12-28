array = [int(el) for el in input().split(',')]
other = []
zeros = []
for el in array:
    if el == 0:
        zeros.append(el)
    else:
        other.append(el)

final_array = other + zeros
print(*final_array, sep=',')
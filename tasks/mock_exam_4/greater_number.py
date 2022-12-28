first_array = [int(el) for el in input().split(',')]
second_array = [int(el) for el in input().split(',')]
final_array = []
for el in first_array:
    if el in second_array:
        index_el = second_array.index(el)
        for i in second_array[index_el + 1:]:
            if i > el:
                final_array.append(str(i))
                break
        else:
            final_array.append('-1')
print(','.join(final_array))


# POINTS = 100






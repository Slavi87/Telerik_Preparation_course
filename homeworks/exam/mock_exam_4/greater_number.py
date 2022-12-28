first_array = [int(el) for el in input().split(',')]
second_array = [int(el) for el in input().split(',')]
final_array = []
for first_num in first_array:
    index_first_num = second_array.index(first_num)
    for second_num in second_array[index_first_num + 1 :]:
        if second_num > first_num:
            final_array.append(second_num)
            break
    else:
        final_array.append(-1)
print(','.join(str(x) for x in final_array))



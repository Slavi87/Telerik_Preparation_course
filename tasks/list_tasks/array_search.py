array = [int(el) for el in input().split(',')]
length = len(array)
new_array = []
final_array = []
for i in range(1, length + 1, 1):
    new_array.append(i)
for el in new_array:
    if el in array:
        continue
    else:
        final_array.append(el)
print(*final_array, sep=',')


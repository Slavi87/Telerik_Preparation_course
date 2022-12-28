array = [int(el) for el in input().split(',')]
length = len(array)
final_array = []
for i in range(1, length + 1):
    if i not in array:
        final_array.append(i)
final_array.sort()
print(*final_array, sep=',')
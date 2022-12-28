input_list = input().split(', ')
numbers = []
for x in input_list:
    numbers.append(int(x))
numbers.sort()
numbers.reverse()
print(*numbers, sep=', ')


size_and_jumps = input().split(' ')
path = input().split(' ')
list_size_and_jumps = []
path_list = []
size = 0
jump_step = 0
growth_balance = 0
for i in size_and_jumps:
    list_size_and_jumps.append(int(i))
    size = list_size_and_jumps[0]
for x in list_size_and_jumps:
    jump_step = list_size_and_jumps[1]
length_snake = size    
for i in path:
    path_list.append(int(i))
for j in range(len(path_list)):
    growth_balance = path_list[j] * jump_step
    length_snake += int(growth_balance)
print(f'{length_snake} {growth_balance}')



# print(size_and_jumps)
# print(path)
# print(list_size_and_jumps)
# print(path_list)
# print(size)
# print(jump_step)
# print(growth_balance)
# print(length_snake)


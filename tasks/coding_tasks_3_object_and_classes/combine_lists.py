first_list = input().split(',')
second_list = input().split(',')
final_list = []
for i in range(len(first_list)):
    final_list.append(first_list[i])
    for j in range(len(second_list)):
        final_list.append(second_list[j])
        second_list.remove(second_list[j])
        break
print(*final_list, sep=',')

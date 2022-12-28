number_spawn_points = int(input())
indices_safe_house = [int(el) for el in input().split()]
spawn = []
number_the_same = False
final_spaw = []
max_num = 0
for i in range(number_spawn_points):
    if i in indices_safe_house:
        spawn.append('0')
    else:
        spawn.append('1')
safe_houses_number = len(indices_safe_house)
if safe_houses_number == 1:
    for k in range(indices_safe_house[0], 0, -1):
        final_spaw.append(k)
        k -= 1
    for j in range(indices_safe_house[0], len(spawn)):
        final_spaw.append(j - indices_safe_house[0])
        j += 1
    max_num = max(final_spaw)
elif safe_houses_number == 2:
    length_between_indices = abs(indices_safe_house[0] - indices_safe_house[1])
    max_num = length_between_indices / safe_houses_number
elif safe_houses_number == 3:
    if number_spawn_points == safe_houses_number:
        number_the_same = True
    else:
        length = abs(indices_safe_house[0] - indices_safe_house[1])
        second_length = abs(indices_safe_house[1] - indices_safe_house[2])
        max_num = max(length, second_length)

if number_the_same:
    print('0 0 0')
else:
    print(int(max_num))

# POINTS = 75


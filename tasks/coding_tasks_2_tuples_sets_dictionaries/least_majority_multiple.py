first_num = int(input())
second_num = int(input())
third_num = int(input())
fourth_num = int(input())
fifth_num = int(input())
counter = 0
searched_num = 0
for i in range(1, 1000000):
    if i % first_num == 0:
        counter += 1
    if i % second_num == 0:
        counter += 1
    if i % third_num == 0:
        counter += 1
    if i % fourth_num == 0:
        counter += 1
    if i % fifth_num == 0:
        counter += 1
    if counter >= 3:
        it_find = True
        searched_num = i
        print(searched_num)
        break
    counter = 0


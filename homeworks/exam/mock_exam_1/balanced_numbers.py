num_lst = []
while True:
    number = input()
    if int(number[0]) + int(number[2]) == int(number[1]):
        num_lst.append(int(number))
    else:
        break

print(sum(num_lst))
lst_numbers = [el for el in input().split(',')]
n = int(input())
for i in range(n):
    lst_numbers.append(lst_numbers[0])
    lst_numbers.pop(0)
print(*lst_numbers, sep=',')

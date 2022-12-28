n = int(input())
k = int(input())
my_factorial_1 = 1
my_factorial_2 = 1
for number in range(1, n + 1):
    my_factorial_1 *= number
for el in range(1, k + 1):
    my_factorial_2 *= el
final_factorial = my_factorial_1 / my_factorial_2
print(f'{int(final_factorial)}')

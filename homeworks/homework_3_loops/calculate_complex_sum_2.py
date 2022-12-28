n = int(input())
x = float(input())
complex = 1
my_factorial = 1
for number in range(1, n + 1):
    my_factorial *= number
    complex = complex + my_factorial / x ** number
print(f'{complex:.5f}')



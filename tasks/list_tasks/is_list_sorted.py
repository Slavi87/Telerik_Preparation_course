n = int(input())
for i in range(n):
    numbers = [int(el) for el in input().split(',')]
    if numbers == sorted(numbers):
        print('true')
    else:
        print('false')
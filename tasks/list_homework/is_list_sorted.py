numbers = [int(el) for el in input().split()]
if numbers == sorted(numbers):
    print('Yes')
else:
    print('No')
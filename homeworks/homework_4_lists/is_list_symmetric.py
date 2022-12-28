numbers = [int(el) for el in input().split()]
numbers_is_symmetric = False
while len(numbers) > 1:
    if len(numbers) % 2 == 0:
        if numbers[0] == numbers[-1]:
            numbers.remove(numbers[0])
            numbers.remove(numbers[-1])
            if len(numbers) == 0:
                numbers_is_symmetric = True
        elif numbers[0] != numbers[1]:
            break
    elif len(numbers) % 2 != 0:
        if numbers[0] == numbers[-1]:
            numbers.remove(numbers[0])
            numbers.remove(numbers[-1])
            if len(numbers) == 1:
                numbers_is_symmetric = True
        elif numbers[0] != numbers[1]:
            break
if numbers_is_symmetric:
    print('Yes')
else:
    print('No')
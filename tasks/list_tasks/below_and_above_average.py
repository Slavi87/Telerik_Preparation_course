numbers = [int(el) for el in input().split(',')]
below_numbers = []
above_numbers = []
average_sum = sum(numbers) / len(numbers)
for el in numbers:
    if el > average_sum:
        above_numbers.append(str(el))
    elif el < average_sum:
        below_numbers.append(str(el))
    else:
        continue
print(f'avg: {average_sum:.2f}')
print(f'below: {",".join(below_numbers)}')
print(f'above: {",".join(above_numbers)}')
def arrangement(numbers):
    if numbers[0] < numbers[1] < numbers[2] < numbers[3]:
        return 'Ascending'
    elif numbers[0] > numbers[1] > numbers[2] > numbers[3]:
        return 'Descending'
    else:
        return 'Mixed'


nums = [int(el) for el in input().split()]
print(arrangement(nums))
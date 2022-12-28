target_sum = int(input())
numbers = [int(el) for el in input().split()]
for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            print(f'{numbers[i]}, {numbers[j]}')
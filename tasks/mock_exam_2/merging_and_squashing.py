n = int(input())
numbers = []
merged_numbers = []
squashed_numbers = []
squashed_num_one = ''
squashed_num_two = ''
squashed_num_tree = ''
merged_num_one = ''
merged_num_two = ''
for el in range(n):
    number = input()
    numbers.append(number)
for i in range(0, len(numbers)):
    merged_num_one = numbers[i][1]
    merged_num_two = numbers[i + 1][0]
    merged_numbers.append(merged_num_one + merged_num_two)
    if len(numbers) - 1 == len(merged_numbers):
        break
for j in range(0, len(numbers)):
    squashed_num_one = numbers[j][0]
    squashed_num_two = int(numbers[j][1]) + int(numbers[j + 1][0])
    if squashed_num_two > 9:
        squashed_num_two = squashed_num_two - 10
    squashed_num_tree = numbers[j + 1][1]
    squashed_numbers.append(squashed_num_one + str(squashed_num_two) + squashed_num_tree)
    if len(numbers) - 1 == len(squashed_numbers):
        break
print(' '.join(merged_numbers))
print(' '.join(squashed_numbers))

# POINTS = 100
sequence = [int(el) for el in input().split()]
counter = 0
max_counter = 0
number = 0
my_sequence = []
max_sequence = []
for i in sequence:
    if i > number:
        number = i
        counter += 1
        my_sequence.append(i)
        max_counter = counter
        if len(my_sequence) >= len(max_sequence):
            max_sequence = my_sequence
    elif i <= number:
        counter = 1
        number = i
        my_sequence = []
        my_sequence.append(i)
print(*max_sequence, sep=' ')


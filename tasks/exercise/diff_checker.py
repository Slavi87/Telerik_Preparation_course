
first_array = [int(el) for el in input().split()]
second_array = [int(el) for el in input().split()]
if len(first_array) > len(second_array):
    for i in range(len(second_array)):
        if first_array[i] == second_array[i]:
            print(f'+ {first_array[i]} {second_array[i]}')
        else:
            print(f'- {first_array[i]} {second_array[i]}')
    length = len(second_array)
    for el in first_array[length:]:
        print(f'- {el} x')
elif len(first_array) < len(second_array):
    for i in range(len(first_array)):
        if first_array[i] == second_array[i]:
            print(f'+ {first_array[i]} {second_array[i]}')
        else:
            print(f'- {first_array[i]} {second_array[i]}')
    length_two = len(first_array)
    for el in second_array[length_two:]:
        print(f'- {el} x')
elif len(first_array) == len(second_array):
    for i in range(len(first_array)):
        if first_array[i] == second_array[i]:
            print(f'+ {first_array[i]} {second_array[i]}')
        else:
            print(f'- {first_array[i]} {second_array[i]}')


number = int(input())
counter_string = 0
counter_numbers = 0
sum_numbers = 0
num_lst = []
string = []
iteration_counter = []
while number > 0:
    command = input()
    if command.isalpha():
        string.append(command)
        counter_string += 1
        iteration_counter.append(counter_string)
    else:
        num_lst.append(command)
        counter_numbers += 1
        iteration_counter.append(counter_numbers)




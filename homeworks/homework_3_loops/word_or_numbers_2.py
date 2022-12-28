number = int(input())
sum_numbers = 0
string = []
while number > 0:
    command = input()
    if command.isalpha():
        string.append(command)
    else:
        sum_numbers += int(command)
    number -= 1 
if len(string) == 0:
    print('no words')
else:
    print('-'.join(string))
print(sum_numbers)        

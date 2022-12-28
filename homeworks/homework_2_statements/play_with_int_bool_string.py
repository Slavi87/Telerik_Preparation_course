print('Please choose a type:')
user = int(input())
if user == 1:
    print(f'{user + 1}')
if user == 2:
    print('Please enter a bool:')
    boolian = input()
    if boolian == 'True':
        print('False')
    elif boolian == 'False':
        print('True')
if user == 3:
    print('Please enter a string:')
    string = input()
    print(f'{string}*')






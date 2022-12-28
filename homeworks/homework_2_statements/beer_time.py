time = input()
char = time[-2]

if char == 'P':
    if time[0] >= "1":
        print('beer time')
    else:
        print('non-beer time')
elif char == 'A':
    if time[0] == '0':
        if time[1] > "2":
            print('non-beer time')
        elif time[1] <= '2':
            print('beer time')
    elif time[0] != '0':
        if time[0] > '2':
            print('non-beer time')
        else:
            print('beer time')

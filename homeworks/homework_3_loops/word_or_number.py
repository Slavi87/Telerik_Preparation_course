while True:
    command = input()
    if command.isalpha():
        string = command[::-1]
        print(string)
    else:
        if command.isdecimal() or float(command) < 0:
            numbers = int(command) + 1
            print(numbers)
        else:
            numbers = float(command) + 1
            print(f'{numbers:.2f}')


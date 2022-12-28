commands = list(input())
x = 0
y = 0
for command in commands:
    if command == 'D':
        y -= 1
    elif command == 'U':
        y += 1
    elif command == 'R':
        x += 1
    elif command == 'L':
        x -= 1
print(f'({x}, {y})')                    
a = input()
b = input()
c = input()
if float(a) > float(b) and float(a) > float(c):
    print(f'{a}')
elif float(b) > float(a) and float(b) > float(c):
    print(f'{b}')
elif float(c) > float(a) and float(c) > float(b):
    print(f'{c}')        
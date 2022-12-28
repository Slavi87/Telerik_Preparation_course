a = input()
b = input()
c = input()
if float(a) >= float(b) and float(a) >= float(c):
    if float(b) >= float(c):
        print(f'{a} {b} {c}')
    else:
        print(f'{a} {c} {b}')
elif float(b) >= float(a) and float(b) >= float(c):
    if float(a) >= float(c):
        print(f'{b} {a} {c}')
    else:
        print(f'{b} {c} {a}')      
elif float(c) >= float(a) and float(c) >= float(b):
    if float(a) >= float(b):
        print(f'{c} {a} {b}')
    else:
        print(f'{c} {b} {a}')                  
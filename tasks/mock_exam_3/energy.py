number = input()
sum_even_digits = 0
sum_odd_digits = 0
for el in number:
    if int(el) % 2 == 0:
        sum_even_digits += int(el)
    else:
        sum_odd_digits += int(el)
if sum_even_digits > sum_odd_digits:
    print(f'{sum_even_digits} energy drinks')
elif sum_even_digits < sum_odd_digits:
    print(f'{sum_odd_digits} cups of coffee')
else:
    print(f'{sum_even_digits} of both')



# POINTS = 100
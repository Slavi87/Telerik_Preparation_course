balanced_numbers = []
while True:
    number = input()
    if int(number[1]) == int(number[0]) + int(number[2]):
        balanced_numbers.append(int(number))
    else:
        break
print(sum(balanced_numbers))



# POINTS = 100

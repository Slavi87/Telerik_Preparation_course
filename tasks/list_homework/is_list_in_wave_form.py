numbers = [int(el) for el in input().split()]
is_wave_form = False
for i in range(0, (len(numbers)-1), 2):
    if numbers[i] > numbers[i + 1] and numbers[i + 1] < numbers[i]:
        is_wave_form = True
    else:
        is_wave_form = False
        break
if is_wave_form:
    print('Yes')
else:
    print('No')


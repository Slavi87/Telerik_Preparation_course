numbers = [int(el) for el in input().split()]
odd_product = 1
even_product = 1
for el in range(len(numbers)):
    if el % 2 == 0:
        odd_product *= numbers[el]
    else:
        even_product *= numbers[el]
# for i, v in enumerate(numbers):
#     if i % 2 == 0:
#         odd_product *= v
#     else:
#         even_product *= v
if odd_product == even_product:
    print('yes')
else:
    print('no')



number_lst = [input() for _ in range(5)]
products = ''
for el in number_lst:
    first_digit = el[0]
    second_digit = el[1]
    third_digit = el[2]
    product = int(first_digit) * int(second_digit) * int(third_digit)
    string_product = str(product)
    if len(string_product) == 1:
        products += string_product
    elif len(string_product) > 1:
        products += string_product[-1]
print(products)

# POINT = 100




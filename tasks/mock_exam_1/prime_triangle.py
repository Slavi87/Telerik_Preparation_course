n = int(input())
prime_lst = []
for el in range(1, n + 1):
    for i in range(2, el):
        if el % i == 0:
            break
    else:
        prime_lst.append(el)
for element in prime_lst:
    for i in range(1, element + 1):
        if i in prime_lst:
            print('1', end='')
        else:
            print('0', end='')
    print()


# POINT = 100



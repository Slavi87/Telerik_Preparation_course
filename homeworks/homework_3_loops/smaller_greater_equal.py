num = int(input())
last_num = 0
operators = []
nums_lst = []
final_lst = []
for i in range(1, num + 1):
    n = int(input())
    nums_lst.append(n)
    if last_num < n:
        operators.append('<')
    elif n < last_num:
        operators.append('>')
    elif n == last_num:
        operators.append('=')
    last_num = n

operators.pop(0)
operators.append('>')
for number in nums_lst:
    final_lst.append(str(number))
    final_lst.append(operators[0])
    operators.pop(0)
final_lst.pop(-1)

print(''.join(final_lst))




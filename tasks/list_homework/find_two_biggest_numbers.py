numbers = [int(el) for el in input().split()]
lst_max_nums = []
max_num = max(numbers)
lst_max_nums.append(str(max_num))
numbers.remove(max_num)
max_num = max(numbers)
lst_max_nums.append(str(max_num))
print(' '.join(lst_max_nums))
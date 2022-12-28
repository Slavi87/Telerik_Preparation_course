def pin_code(numbers):
    final_nums = []
    for num in numbers:
        new_num = num[::-1]
        final_nums.append(int(new_num))
    max_num = max(final_nums)
    return max_num


nums = [el for(el) in input().split()]
print(pin_code(nums))
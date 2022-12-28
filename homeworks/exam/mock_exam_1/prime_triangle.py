n = int(input())
digits = [0] * 10
max_count = 0
max_index = 0
for i in range(n):
    num = int(input())
    digits[num-1] += 1
    if digits[num-1] > max_count or digits[num-1] == max_count and num - 1 < max_index:
        max_count = digits[num - 1]
        max_index = num - 1
print(max_index + 1)        
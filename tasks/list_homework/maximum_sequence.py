from itertools import groupby
sequence = input().split()
result = [list(y) for x, y in groupby(sequence)]
max_length = 0
for el in result:
    if len(el) > max_length:
        max_length = len(el)
print(max_length)
n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 or i % 7 == 0:
        continue
    print(i, end=' ')    
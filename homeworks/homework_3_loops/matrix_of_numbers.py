number = int(input())
for i in range(1, number + 1):
    for j in range(i, number + i):
        print(j, end=" ")
    print()
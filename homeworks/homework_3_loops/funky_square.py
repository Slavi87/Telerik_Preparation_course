n = int(input())
numbers = " "
for i in range(n):
    numbers = numbers[:i] + f"{i + 1}" * (n - i)
    print(' '.join(numbers))

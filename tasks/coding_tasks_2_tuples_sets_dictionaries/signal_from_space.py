message = list(input())
for i in range(len(message) - 1, 0, -1):
    if message[i] == message[i - 1]:
        message.pop(i)
print(*message, sep='')
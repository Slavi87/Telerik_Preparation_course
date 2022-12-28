message = list(input())
index = 0
while index <= len(message) + 1:
    for i in range(index, len(message), 1):
        if i + 1 <= len(message) + 3 and message[i] == message[i + 1]:
            message[i + 1] = ''
        index += 1


print(message)
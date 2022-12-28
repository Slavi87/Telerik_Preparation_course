title = input()
n = int(input())
words = [input() for _ in range(n)]

for word in words:
    temp_title = list(title)
    indices = [0]

    for char in word:
        if char in temp_title[indices[-1]:]:
            current_index = temp_title[indices[-1]:].index(char)
            temp_title[current_index + indices[-1]] = "_"
            indices.append(current_index + indices[-1])

    if len(indices[1:]) == len(word):
        title = []
        for char in temp_title:
            if char != "_":
                title.append(char)

        print("".join(title))
    else:
        print("No such title found!")
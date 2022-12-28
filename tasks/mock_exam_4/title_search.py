title = input()
n = int(input())
words = [input() for i in range(n)]
for word in words:
    current_title = list(title)
    indices = [0]
    for el in word:
        if el in current_title[indices[-1]:]:
            current_index = current_title[indices[-1]:].index(el)
            current_title[current_index + indices[-1]] = '_'
            indices.append(current_index + indices[-1])
    if len(indices) - 1 == len(word):
        title = []
        for i in current_title:
            if i != '_':
                title.append(i)
        print(''.join(title))
    else:
        print("No such title found!")


# POINTS = 100
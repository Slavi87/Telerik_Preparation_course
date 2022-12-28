def electronic_message(message):
    new_text = text[:-1]
    characters = []
    length_lst = []
    for j in range(0, len(new_text)):
        if new_text[j].isdigit() or new_text[j].isalpha() or new_text[j] == ' ':
            length = len(characters)
            length_lst.append(length)
            characters.clear()

        else:
            characters.append(new_text[j])
    max_num = max(length_lst)
    return max_num


text = input()
print(electronic_message(text))
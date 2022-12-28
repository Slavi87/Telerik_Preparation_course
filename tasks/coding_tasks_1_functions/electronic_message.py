def electronic_message(text):
    new_text = text[:-1]
    characters = []
    length_lst = []
    for i in range(len(new_text[::])):
        if new_text[i].isdigit() or new_text[i].isalpha() or new_text[i] == ' ':
            length = len(characters)
            length_lst.append(length)
            characters.clear()
            continue
        else:
            characters.append(new_text[i])
    max_num = max(length_lst)
    return max_num


string = input()
print(electronic_message(string))


# POINTS = 70 INVALID RETURN

# def electronic_message(message):
#     new_text = text[:-1]
#     characters = []
#     length_lst = []
#     for j in range(0, len(new_text)):
#         if new_text[j].isdigit() or new_text[j].isalpha() or new_text[j] == ' ':
#             length = len(characters)
#             length_lst.append(length)
#             characters.clear()
#
#         else:
#             characters.append(new_text[j])
#     max_num = max(length_lst)
#     return max_num
#
#
# text = input()
# print(electronic_message(text))
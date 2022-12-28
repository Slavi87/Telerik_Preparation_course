sentence = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']
final_sentence = []
for word in sentence:
    if word[0].lower() in vowels:
        first_letter = word[0]
        new_word = word[1:] + first_letter + 'che'
        if len(word) % 2 == 0:
            new_word = new_word + 'e'
            final_sentence.append(new_word)
        else:
            final_sentence.append(new_word)
    else:
        if len(word) % 2 == 0:
            new_word = word + 'che' + 'e'
            final_sentence.append(new_word)
        else:
            new_word = word + 'che'
            final_sentence.append(new_word)
print(*final_sentence)


# POINTS = 100
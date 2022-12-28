alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
max_counter = 0
heaviest_word = ''
n = int(input())
for i in range(n):
    word = input()
    counter = 0
    for el in word:
        if el.upper() in alphabet:
            letter_index = alphabet.index(el.upper()) + 1
            counter += letter_index
    if counter > max_counter:
        max_counter = counter
        heaviest_word = word
print(f'{max_counter} {heaviest_word}')

# POINTS = 100
vowels = ['a', 'e', 'i', 'o', 'u']
n = int(input())
max_ratio = 0
max_vowels = 0
words = []
counters_vowels = []
for i in range(n):
    food = input()
    counter_vowels = 0
    length = len(food)
    for el in food:
        if el in vowels:
            counter_vowels += 1
    ratio = length / counter_vowels
    if ratio > max_ratio:
        max_ratio = ratio
        words.append(food)
        counters_vowels.append(int(counter_vowels))
        max_vowels = counter_vowels
    elif ratio == max_ratio:
        words.append(food)
        counters_vowels.append(int(counter_vowels))
if len(words) > 1:
    index_word = []
    max_num = max(counters_vowels)
    for j in counters_vowels:
        if j == max_num:
            index = counters_vowels.index(j)
            index_word.append(words[index])
    if len(index_word) > 0:
        max_length_word = 0
        final_word = ''
        for w in index_word:
            length = len(w)
            if length > max_length_word:
                final_word += w
        print(f'{final_word} {max_num}/{len(final_word)}')
elif len(words) == 1:
    final_word = words[0]
    length = len(final_word)
    print(f'{"".join(words)} {max_vowels}/{length}')




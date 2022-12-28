word = list(input())
n = int(input())
words_lst = []
sum_word = 0
for w in word:
    sum_word += ord(w)
it_is_anagram = False
for i in range(n):
    current_word = input()
    words_lst.append(current_word)
for el in words_lst:
    counter = 0
    if len(word) == len(el):
        total_sum = 0
        for j in el:
            if j in word:
                total_sum += ord(j)
        if total_sum == sum_word:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

# POINTS = 100
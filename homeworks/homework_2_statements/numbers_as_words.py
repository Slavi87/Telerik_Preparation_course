words = "Zero One Two Three Four Five Six Seven Eight Nine" + \
    " Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty" + \
" Thirty Forty Fifty Sixty Seventy Eighty Ninety"
words = words.split(" ")


def number_to_words(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else ' ' + words[n % 10])
    elif n < 1000:
        return number_to_words(n // 100) + " hundred" + (' ' + number_to_words(n % 100) if n % 100 > 0 else '')


n = int(input())
print(number_to_words(n))
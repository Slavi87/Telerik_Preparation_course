def valid_sign(sign):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    if sign in cards:
        print('yes')
    else:
        print('no')


card = input()
valid_sign(card)
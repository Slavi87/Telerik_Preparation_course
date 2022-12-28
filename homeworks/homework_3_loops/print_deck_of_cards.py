for number in range(2, 15):
    if number > 10:
        if number == 11:
            print('J of spades, J of clubs, J of hearts, J of diamond')
        if number == 12:
            print('D of spades, D of clubs, D of hearts, D of diamond')
        if number == 13:
            print('K of spades, K of clubs, K of hearts, K of diamond')
        if number == 14:
            print('A of spades, A of clubs, A of hearts, A of diamond')
    else:
        print(f'{number} of spades, {number} of clubs, {number} of hearts, {number} of diamond')                




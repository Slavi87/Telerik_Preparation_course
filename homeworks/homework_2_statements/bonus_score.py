number = int(input())
if 1 <= number <= 3:
    number *= 10
    print(number)
elif 4 <= number <= 6:
    number *= 100
    print(number)
elif 7 <= number <= 9:
    number *= 1000
    print(number)
else:
    print('invalid score')   
        
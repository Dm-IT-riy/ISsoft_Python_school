num_1, num_2 = int(input('Enter number 1: ')), int(input('Enter number 2: '))
i, j = num_1, num_2

while(i and j):
    if (i > j):
        i %= j
    else:
        j %= i

if(i + j == 1):
    print(f'{num_1} и {num_2} взаимопростые')
else:
    print(f'{num_1} и {num_2} невзаимопростые')
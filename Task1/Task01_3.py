decimal_number = input('Enter decimal number: ')
sum = 0
symbols = ['.', '-', ',']

for number in decimal_number:
    flag = True
    for symbol in symbols:
        if number == symbol:
            flag = False
            continue
    if flag:
        sum += int(number)

print(f'Sum: {sum}')
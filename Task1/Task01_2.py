string, letter = input('Enter any string: '), input('Enter any letter: ')
print(f'«Буква {letter}',
    'встречается' if letter in string else 'не встречается',
    f'в строке {string}»')

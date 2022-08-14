a = int(input('Enter rectangle length: '))
b = int(input('Enter rectangle width: '))
c = int(input('Enter square length: '))

if a < c or b < c:
   print(f'Квадрат не поместится')
else:
    print(f'Поместится {(a//c) * (b//c)}')

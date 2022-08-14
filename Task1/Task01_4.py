number = int(input('Enter positive integer number: '))
count = 0

for i in range(2, number + 1):
    if number % i:
        continue

    simple = True
    for j in range(2, i):
        if not i % j:
            simple = False
            break
    if simple:
        count += i
if number <= 0:
    print('Enter number > 0!')
else:
    print(count if count != number and number != 1 else
        f'Простых делителей нет, число делится само на себя: {number}')
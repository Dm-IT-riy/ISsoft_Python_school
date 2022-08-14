with open('task2.txt') as f:
    text = f.read().lower()

#Убираем все лишние символы для работы именно с латинским алфавитом
#Т.к. не регулярки, скорость циклом режется
rep = ['.', ',', '-', '!', '"', "'", '1', '2', '3', '4', '5', '6', '7', '8',
    '9', '0', '<', '>', '/', '\\', '?', ';', ':', '`', '@', '#', '№', '$',
    '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']
for item in rep:
    if item in text:
        text = text.replace(item, ' ')

words = text.split()
unique_words = set(text.split())
 
data = sorted(zip([words.count(x) for x in unique_words], unique_words),
    reverse=True)
result = []
for i in data:  
    if(i[0] >= data[0][0]):
        result += i

print(f'Самое частовстречаемое слово: {result[1::2]}. ',
    f'Количество встреч: {result[0]}')
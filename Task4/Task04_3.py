with open('task3_1.txt') as f1:
    text1 = f1.read().lower()

with open('task3_2.txt') as f2:
    text2 = f2.read().lower()

print(set(text1.split()) & set(text2.split()))
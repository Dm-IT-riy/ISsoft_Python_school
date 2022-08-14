def gen(*n):
    if not n:
        k = 1
        while(True):
            yield factorial(k)
            k += 1
    else:
        for i in range(1, n[0] + 1):
            yield factorial(i)      

def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n -1)

my_gen = gen(10)

while(True):
    item = next(my_gen)
    print(item)
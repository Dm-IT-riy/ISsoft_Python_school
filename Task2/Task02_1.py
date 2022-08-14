def parity(*args):
    i = 1
    if len(args):
        stop = args[0]
        while(i <= stop):
            yield i
            i += 1
    else:
        while(True):
            yield i
            i += 1

for i in parity(100):
    print(f'{i} - чётное' if not i % 2 else f'{i} - нечётное')
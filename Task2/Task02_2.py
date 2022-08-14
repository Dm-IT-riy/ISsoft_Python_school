def primes(*args):
    i = 1
    if len(args):
        stop = args[0]
        while(i < stop):
            i += 1
            if isprime(i):
                yield i
    else:
        while(True):
            i += 1
            if isprime(i):
                yield i


def isprime(n):
    simple = True
    for i in range(2, n):
        if not n % i:
            simple = False
            break
    if simple:
        return(n)

for i in primes(100):
    print(i)
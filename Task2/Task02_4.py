def conditions(*args):
    def cond(current):
        if len(args):
            return current <= args[0]
        else:
            return True
    return cond

def gen(*args):
    condition = conditions(*args)
    current = 10
    num_digits = 2
    while condition(current):
        if is_palindrome(current, num_digits):
            yield current
        current += 1
        if current // (10**num_digits):
            num_digits += 1

def is_palindrome(number, number_digit):
    if number_digit <= 1:
        return True
    elif number % 10 != number // (10**(number_digit - 1)):
        return False
    else:
        number %= 10**(number_digit - 1)
        number //= 10
        return is_palindrome(number, number_digit - 2)

for num in gen(1000):
    print(num)
number = 0

begin_system = int(input('Enter begin number system: '))
end_system = int(input('Enter end number system: '))


def system_to_num(num_sys, base = None):
    digit = input('Enter digit: ')
    if digit:
        digit = int(digit)
        base = 0

        global number
        number += digit * (num_sys ** base)
        return base + 1
    else:
        return 0


def num_to_system(num_sys):
    global number
    if not number:
        return

    digit = number % num_sys
    number //= num_sys

    num_to_system(num_sys)
    print(digit, end='')

system_to_num(begin_system)
num_to_system(end_system)

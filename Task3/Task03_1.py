number = input('Enter digit: ')
start_base = int(input('Enter begin number system: '))
end_base = int(input('Enter end number system: '))
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def toBaseInt(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base] 
    while n >= base:
        n = n // base
        b += alpha[n % base] 
    return ('' if num >= 0 else '-') + b[::-1] 
    
def toBaseFrac(frac, base, n = 16):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ''
    while n:
        frac *= base
        frac = round(frac, n)
        b += str(alpha[int(frac)])
        frac -= int(frac)
        n -= 1
    return b

if '.' in number:
    num, frac = map(str, number.split('.'))
    num = int(num, start_base)
    a = toBaseInt(num, end_base)
    b = 0
    k = start_base
    for i in frac:
        b += alpha.index(i) / k
        k *= start_base
    b = str(toBaseFrac(b, end_base)).rstrip('0')
    print(f'{a}.{b}({end_base})')
else:
    print(f'{toBaseInt(int(number, start_base), end_base)}({end_base})')
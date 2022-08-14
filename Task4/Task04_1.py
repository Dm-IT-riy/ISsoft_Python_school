morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'}

src = 'task1.txt'

def encryption(path):
    try:
        with open(path) as f:
            text = f.read()
    except Exception as ex:
        print(ex, f'Please, create a file "{path}" and try again.', sep = '\n')
        exit()
    result = []
    for word in text.lower().split():
        char = []
        for i in word:
            char.append(morse_code[i])
        result.append(' '.join(char))
    with open('cod.' + path, 'w') as f:
        f.write('   '.join(result))

def decryption(path):
    try:
        with open('cod.' + path) as f:
            text = f.read()
    except Exception as ex:
        print(ex, f'Please, create a file "cod.{path}" and try again.', sep = '\n')
        exit()
    result = []
    for word in text.split('   '):
        symbol = []
        for i in word.split():
            for key, value in morse_code.items():
                if i == value:
                    symbol.append(key)
        result.append(''.join(symbol))
    result[0] = result[0].capitalize()
    with open(path, 'w') as f:
        f.write(' '.join(result))

encryption(src)
decryption(src)
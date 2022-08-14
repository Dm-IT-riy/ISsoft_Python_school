string = input('Enter some string: ')


def reverse(string):
    words_list = [i for i in string.split(" ")]
    result = ""
    for some_word in words_list:
        some_word = [i for i in some_word]
        right = len(some_word) - 1
        left = 0
        while left < right:
            if not (some_word[left].isalpha() or some_word[left].isdigit()):
                left += 1
            elif not (some_word[right].isalpha() or some_word[right].isdigit()):
                right -= 1
            else:
                some_word[left], some_word[right] = some_word[right], some_word[left]
                left += 1 
                right -= 1
        word = "".join(some_word)
        result += (word+" ")
    return result

print(reverse(string))
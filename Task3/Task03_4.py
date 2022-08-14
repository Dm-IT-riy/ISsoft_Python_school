list = [1, 2, 7, 1, 3, 2, 4, 7, 2, 1, 'a', 'a', 'a', 'a', True, [8, 8, 8], '1']

list1 = []
for i in list:
    k = f'{i}'
    list1.append(k)

def split_list(list):
    frequency = {}
    for item in list:
        if item not in frequency:
            frequency[item] = list.count(item)

    arrays = {}
    for freq in frequency.values():
        if freq not in arrays:
            arrays[freq] = []

    for item in list:
        arrays[frequency[item]].append(item)

    sort = sorted(arrays.items(), reverse = True)

    return sort

def print_list(list):
    end_list = []
    for item in list:
        for symbol in item[1]:
            symbol = symbol[1:]
        end_list.append(item[1])
    print(end_list)

print_list(split_list(list1))
def k_min(seq, k):
    if k < 0 or k >= len(seq):
        return

    base_elem_index = len(seq) // 2
    base_elem = seq[base_elem_index]

    try:
        left = [elem for elem in seq if elem < base_elem]
    except TypeError:
        return

    if len(left) > k:
        return k_min(left, k)

    try:
        middle = [elem for elem in seq if elem == base_elem]
    except TypeError:
        return

    if len(left) + len(middle) > k:
        return middle[k - len(left)]

    try:
        right = [elem for elem in seq if elem > base_elem]
    except TypeError:
        return

    return k_min(right, k - len(left) - len(middle))


lst = [3, 7, 11, True, 2, 8, 5, 2, 7, 1, 0]
print(f'Result: {k_min(lst, 7)}')
def no_repeat(src):
    count_dict = {}
    result = {}
    for val in src:
        count_dict.setdefault(val, 0)
        count_dict[val] = count_dict.get(val) + 1
        if count_dict[val] <= 1:
            result.setdefault(val, 1)
        else:
            result.pop(val, 0)
    return result.keys()


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(*no_repeat(src))



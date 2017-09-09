def value_of(name):
    name = name.lower()
    value = sum([ord(c) - ord('a') + 1 for c in name])
    # print ("value of {} is {}".format(name, value))
    return value


def compare(a, b):
    va = value_of(a)
    vb = value_of(b)
    if va == vb:
        return cmp(a, b)
    return va - vb


def answer(names):
    return sorted(names, cmp=compare, reverse=True)


names = ["annie", "bonnie", "liz"]
names = ["abcdefg", "vi"]
names = ["AL", "CJ"]
print(answer(names))

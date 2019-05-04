def string_combinations(s):
    l = len(s)
    for i in range(1, l):
        for j in range(l - i + 1):
            print(s[0:j] + s[j + i:])


def string_combinations2(s):
    level = ['']
    for i in range(len(s)):
        nlist = []
        for item in level:
            nlist.append(item + s[i])
        level += nlist

    return level[1:]


print(string_combinations2('abc'))

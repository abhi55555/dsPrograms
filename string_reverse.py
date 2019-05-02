def strReverse1(s):
    return s[::-1]


def strReverse2(s):
    l = len(s) // 2
    sli = []
    [sli.append(ch) for ch in s]
    for i in range(l):
        sli[i], sli[-(i + 1)] = sli[-(i + 1)], sli[i]

    res = ''.join(sli)
    return res


def strReverse3(s):
    res = ''
    for ch in s:
        res = ch + res
    return res


def strReverse4(s):
    res = ''.join(reversed(s))
    return res


def strReverse5(s):
    if len(s) == 0:
        return s
    else:
        return strReverse5(s[1:]) + s[0]


new_str = 'asdfreqrougfwbogheqgbqwognfnqoubcqbeigfcvwibvwjrwigqhpvnapfjedknc;;NVBWBVWOJBqwertyaaaaaaa'
print(strReverse3(new_str))

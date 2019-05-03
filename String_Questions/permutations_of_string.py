def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[i], a[l] = a[l], a[i]
            permute(a, l + 1, r)
            a[i], a[l] = a[l], a[i]  # putting back in original position during backtracking


string = 'abcd'
n = len(string)
a = list(string)

permute(a, 0, n - 1)

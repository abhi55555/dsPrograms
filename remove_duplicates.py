def removeDuplicates(A):
    table = {}
    for a in A:
        if a in table:
            table[a] += 1
        elif a not in table:
            table[a] = 1
        else:
            table[a] += 0

    newtable = []
    [newtable.append(t) for t in table.keys()]
    print(newtable)


def removeDuplicates2(A):
    unique = []
    heplerSet = set()
    for x in A:
        if x not in heplerSet:
            unique.append(x)
            heplerSet.add(x)

    print(unique)


def removeDuplicates3(A):
    print(list(dict.fromkeys(A)))


A = [4, 2, 2, 3, 22, 3, 3, 14, 5, 17, 9]

removeDuplicates3(A)

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


A = [4, 2, 2, 3, 22, 3, 3, 14, 5, 17, 9]

removeDuplicates(A)

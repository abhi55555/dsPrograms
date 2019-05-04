def removeDuplicates(A):
    table = {}
    for a in A:
        if a in table:
            table[a] += 1
        else:
            table[a] = 1

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


def removeDuplicates_sorted(A):         # requires sorted array

    j = 0
    for i in range(1, len(A)):
        if A[j] != A[i]:
            j += 1
            A[j] = A[i]

    print(A[:j + 1])


A = [4, 2, 2, 3, 22, 3, 3, 14, 5, 17, 9]
A_sorted = [0, 2, 2, 2, 3, 3, 4, 5, 7, 9]
removeDuplicates3(A)
removeDuplicates_sorted(A_sorted)

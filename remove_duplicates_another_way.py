def removeDuplicates(A):
    unique = []
    heplerSet = set()
    for x in A:
        if x not in heplerSet:
            unique.append(x)
            heplerSet.add(x)

    print(unique)


A = [4, 2, 2, 3, 22, 3, 3, 14, 5, 17, 9]

removeDuplicates(A)

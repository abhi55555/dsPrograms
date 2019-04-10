def checkDuplicates(A):
    table = {}
    for a in A:
        if a in table:
            table[a] += 1
        elif a not in table:
            table[a] = 1
        else:
            table[a] += 0
    # print(table)
    for t in table.keys():
        print(t, end=' ')
    print('\n')
    for a in table:
        if table[a] > 1:
            print('Element repeated first is', a)
            return


A = [3, 2, 1, 45, -12, 0.0002, 2, 82, 3]
checkDuplicates(A)

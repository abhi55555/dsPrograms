# program to check if two arrays have same elements


def checkTwoArrays(A, B):
    table = {}
    for a in A:
        if a in table:
            table[a] += 1
        elif a not in table:
            table[a] = 1
        else:
            table[a] += 0
    # print(table)

    for b in B:
        if b in table and table[b] > 0:
            table[b] -= 1

    for element in table:
        if table[element] != 0:
            print('Arrays are different')
            return

    print('Arrays have same elements')


A = [3, 63, 2, 7, 3, 8, 6, 358, 53, 1]
B = [3, 6, 358, 53, 1, 3, 63, 2, 7]

checkTwoArrays(A, B)

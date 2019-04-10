# finding maximum repitions using hash table


def maxRepitions(A):
    table = {}
    max = 0
    for a in A:
        if a in table:
            table[a] += 1
        elif a != ' ':
            table[a] = 1
        else:
            table[a] += 0
    print(table)
    for element in A:
        if table[element] > max:
            max = table[element]
            maxrep = element
    print(f'{maxrep} repeated for {max} times')


A = [1, 4, 2, 2, 6, 4, 7, 4, 9]

maxRepitions(A)

# find element repeated in array certain number of times


def findElement(A):
    table = {}
    for a in A:
        if a in table:
            table[a] += 1
        elif a not in table:
            table[a] = 1
        else:
            table[a] += 0

    for t in A:
        table[t] == '3':
        print(t)


A = [4, 2, 2, 3, 22, 3, 3, 14, 5, 17, 9, 26]

findElement(A)

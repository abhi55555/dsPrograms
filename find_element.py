# find element repeated in array certain number of times


def findElement(A, n):
    table = {}
    for a in A:
        if a in table:
            table[a] += 1
        elif a not in table:
            table[a] = 1
        else:
            table[a] += 0

    for t in table:
        if table[t] == n:
            print(t)


A = [4, 2, 2, 66, 22, 66, 66, 14, 5, 17, 9, 26]

findElement(A, 3)

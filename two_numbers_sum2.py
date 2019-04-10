# a in array A and b in array B. Find a + b = k for a number k


def twoElements(largearray, smallarray, k):
    s = set(smallarray)

    for l in largearray:
        if (k - l) in s:
            print('Pairs are', l, k - l)

    # table = {s: None for s in smallarray}
    # print(table)
    # for l in largearray:
    #     if (k - l) in table:
    #         print('Pairs are', l, k - l)


A = [5, 7, 3, 7, 9, 4, 21, 6, 9, 4, 677, 3]
B = [2, 5, 8, 5, 2, 9]

twoElements(A, B, 15)

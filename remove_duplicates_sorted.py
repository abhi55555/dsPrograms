def removeDuplicates(A):

    j = 0
    for i in range(1, len(A)):
        if A[j] != A[i]:
            j += 1
            A[j] = A[i]

    print(A[:j + 1])


A = [0, 2, 2, 2, 3, 3, 4, 5, 7, 9]

print(A)
removeDuplicates(A)

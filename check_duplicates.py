def checkDuplicates(A):
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            print('Duplicates found')
            return
    print('Not found')


A = [2, 6, 3, 7, 4, 90, 6]
checkDuplicates(sorted(A))

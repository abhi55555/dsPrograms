def selectionSort(A):
    for i in range(len(A)):
        least = i
        for j in range(i + 1, len(A)):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]


Arr = [32, 1444, 11, 9, 1, 90, 23, 999, 0, -23, -4, 65, 32, 980, -987, -453, 82, 144, 22.5, 57.12]

selectionSort(Arr)
print(Arr)

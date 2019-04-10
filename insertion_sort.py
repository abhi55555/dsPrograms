def insertionSort(A):
    for i in range(1, len(A)):
        temp = A[i]
        k = i
        while(k > 0 and temp < A[k - 1]):
            A[k] = A[k - 1]
            k -= 1
        A[k] = temp
        # print(*A, sep=' ') for debugging


Arr = [32, 1444, 11, 9, 1, 90, 23, 999, 0, -23, -4, 65, 32, 980, -987, -453, 82, 144, 22.5, 57.12]

insertionSort(Arr)
print(Arr)

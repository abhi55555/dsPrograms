def bubbleSort(A):
    for i in range(len(A)):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
            # print(*A, sep=' ') or print(" ".join(map(str, Arr))) for debugging


Arr = [32, 1444, 11, 9, 1, 90, 23, 999, 0, -23, -4, 65, 32, 980, -987, -453, 82, 144, 22.5, 57.12]

bubbleSort(Arr)
print(Arr)

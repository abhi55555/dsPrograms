def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i += 1
            else:
                A[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            A[k] = righthalf[j]
            j += 1
            k += 1


Arr = [32, 1444, 11, 9, 1, 90, 23, 999, 0, -23, -4, 65, 32, 980, -987, -453, 82, 144, 22.5, 57.12]

mergeSort(Arr)
print(Arr)

def shellSort(A):
    sublistcount = len(A) // 2
    while(sublistcount > 0):
        for startposition in range(sublistcount):
            GapInsertionSort(A, startposition, sublistcount)
        # print(f'After increments of size {sublistcount}, the list is {A}')
        sublistcount = sublistcount // 2


def GapInsertionSort(A, start, gap):
    for i in range(start + gap, len(A), gap):
        currentvalue = A[i]
        position = i

        while(position >= gap and A[position - gap] > currentvalue):
            A[position] = A[position - gap]
            position = position - gap
        A[position] = currentvalue


Arr = [32, 1444, 11, 9, 1, 90, 23, 999, 0, -23, -4, 65, 32, 980, -987, -453, 82, 144, 22.5, 57.12]

shellSort(Arr)
print(Arr)

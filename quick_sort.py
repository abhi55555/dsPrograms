
def quickSort(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        quickSort(A, low, pivot - 1)
        quickSort(A, pivot + 1, high)


def partition(A, low, high):
    i = low - 1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]      # puts pivot at its correct position
    return i + 1


Arr = [32, 1444, 11, 9, 1, 90]

quickSort(Arr, 0, len(Arr) - 1)

print(Arr)

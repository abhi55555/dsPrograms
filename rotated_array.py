# find element from where array is rotated


def rotatedArray(A):
    low, high = 0, len(A) - 1
    while(low < high):
        mid = (low + high) // 2
        if A[mid - 1] < A[mid] and A[mid + 1] < A[mid]:
            return A[mid]
        if A[mid] < A[mid + 1]:
            high = mid + 1
        if A[mid] < A[mid - 1]:
            low = mid - 1


A = [15, 16, 18, 22, 1, 3, 5, 7, 14]
print(rotatedArray(A))

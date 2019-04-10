# interpolation search

def interpolationSearch(A, val):
    low = 0
    high = len(A) - 1

    while low <= high and A[low] <= val and A[high] >= val:

        mid = low + ((val - A[low]) * (high - low) // (A[high] - A[low]))

        if val > A[mid]:
            low = mid + 1
        if val < A[mid]:
            high = mid - 1
        if val == A[mid]:
            return (f'Element found at index {mid}')

    return 'Element not found'


A = [1, 4, 6, 9, 12, 19, 29, 45, 67, 89, 100]
print(interpolationSearch(A, 12))

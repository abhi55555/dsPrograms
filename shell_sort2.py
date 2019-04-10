# Python program for implementation of Shell Sort


def shellSort(arr):

    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap = gap // 2


# Driver code to test above
Arr = [32, 11, 9, 1, 90, 23, 999, 0, -23, -4, 65]

shellSort(Arr)
print(Arr)

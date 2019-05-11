# program to implement kadane's algorithm


def max_subarray_sum(arr):
    max_curr = max_sum = arr[0]

    for i in range(1, len(arr)):
        max_curr = max(arr[i], max_curr + arr[i])
        if max_curr > max_sum:
            max_sum = max_curr

    print(max_sum)


array = [3, -1, 2, 4, -9, 1, -5]

max_subarray_sum(array)

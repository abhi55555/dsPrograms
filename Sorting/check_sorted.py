# Program to check array is sorted using recursion
def isSorted(arr):
    # base case
    if len(arr) == 1:
        return True
    return arr[0] <= arr[1] and isSorted(arr[1:])


array = [1, 23, 45, 66, 77, 333]
val = isSorted(array)
print(val)

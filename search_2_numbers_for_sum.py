# a in array A and b in array B. Find a + b = k for a number k


def binarySearch(numlist, val):
    low = 0
    high = len(numlist) - 1

    while low <= high:
        mid = (low + high) // 2
        if numlist[mid] < val:
            low = mid + 1
        if numlist[mid] > val:
            high = mid - 1
        else:
            return mid
    return -1


def findSumInList(A, B, k):
    A.sort()
    for i in range(len(B)):
        c = k - B[i]
        if(binarySearch(A, c) != -1):
            return 'Found'
    return 'Not found'


A = [56, 23, 7]
B = [2, 7, 1]
res = 2340
print(findSumInList(A, B, res))
# it is not working

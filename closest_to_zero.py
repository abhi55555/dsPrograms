# find two nubers in array such that their sum is closest to zero
import sys


def closestToZero(A):
    n = len(A)
    if n < 2:
        print('Array of insufficient length')
        return
    A.sort()
    left = 0
    right = n - 1
    minleft = 0
    minright = n - 1
    minsum = sys.maxsize
    while left < right:
        cursum = A[left] + A[right]
        if abs(cursum) < abs(minsum):
            minsum = cursum
            minleft = left
            minright = right
        if cursum < 0:
            left += 1
        else:
            right -= 1
    print('Required numbers are', A[minleft], A[minright])


A = [23, 46, 34, 322, -35, -56, -32, -33]

closestToZero(A)

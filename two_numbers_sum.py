# find two numbers in array whose sum is k


def findTwoNumbers(A, k):
    n = len(A)
    if n < 2:
        print('Array of insufficient length')
        return
    A.sort()
    left = 0
    right = n - 1

    while(left < right):
        num_sum = A[left] + A[right]
        if num_sum < k:
            left += 1
        if num_sum > k:
            right -= 1
        if num_sum == k:
            print('Required numbers are', A[left], A[right])
            return
    print('No such pair exists')


Arr = [5, 3, 9, 3, 80, -3, 45, 22]

findTwoNumbers(Arr, 67)

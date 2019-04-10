# find three numbers in array whose sum is k


def findThreeNumbers(A, k):
    n = len(A)
    left = 0
    right = n - 1
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while(left < right):
            if(A[i] + A[left] + A[right] == k):
                print('Three numbers are', A[i], A[left], A[right])
                return
            elif(A[i] + A[left] + A[right] < k):
                left += 1
            else:
                right -= 1

    print('No such values found')


A = [1, 6, 45, 5, 34, 67]
A.sort()

findThreeNumbers(A, 74)

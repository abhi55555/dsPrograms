# program to calculate max sum in array with no numbers adjacent to each other.


def maxSumWithNoContinousNumbers(A):  # this is bottom up approach
    n = len(A)
    M = [0] * (n + 1)
    M[0] = A[0]
    if A[1] > A[0]:
        M[1] = A[1]
    for i in range(2, n):
        M[i] = max(A[i] + M[i - 2], M[i - 1])

    return M[n - 1]


Arr = [-2, 3, -16, 100, -4, 5]

print(maxSumWithNoContinousNumbers(Arr))

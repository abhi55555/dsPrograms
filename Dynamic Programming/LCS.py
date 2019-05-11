# program to print length of longest common subsequence
from functools import lru_cache


@lru_cache(maxsize=None)        # using builtin function and decorator for memoization
def LCS(X, Y):
    if not X or not Y:
        return ''
    x, y, m, n = X[0], Y[0], X[1:], Y[1:]
    if x == y:
        return x + LCS(m, n)
    else:
        return max(LCS(X, n), LCS(m, Y), key=len)



def LCS_length(p, q, n, m):
    if arr[n][m] is not None:
        return arr[n][m]
    if n == 0 or m == 0:
        result = 0
    elif p[n - 1] == q[m - 1]:
        return 1 + LCS_length(p, q, n - 1, m - 1)
    else:
        result = max(LCS_length(p, q, n - 1, m), LCS_length(p, q, n, m - 1))
    arr[n][m] = result
    return result


str1 = 'AGGTABAAGGTABAAGGTABAAGGTABAAGGTABAAGGTABAAGGTABAAGGTABAAGGTABAAGGTABAAGGTABAAGGTABA'
str2 = 'GXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYB'
arr = [[None for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]


print(LCS(str1, str2))
# print(LCS_length(str1, str2, len(str1), len(str2)))

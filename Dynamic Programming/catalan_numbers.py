from functools import lru_cache

# @lru_cache(maxsize=1000)


def catalan_num(n):
    if n <= 1:
        return 1
    res = 0

    for i in range(n):
        res += catalan_num(i) * catalan_num(n - i - 1)

    return res


def catalan_num_dynamic(n):
    if n <= 1:
        return 1
    table = [0 for i in range(n + 1)]
    table[0] = 1
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = 0
        for j in range(i):
            table[i] = table[i] + table[j] * table[i - j - 1]

    return table[n]


def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    res = 1

    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res


def catalan_num_using_binomial(n):
    c = binomial_coefficient(2 * n, n)
    return c / (n + 1)


print(catalan_num_using_binomial(6))

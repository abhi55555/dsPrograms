from functools import lru_cache

fibonacci_cache = {}


def fibo2(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = fibo2(n - 1) + fibo2(n - 2)

    fibonacci_cache[n] = result
    return result


@lru_cache(maxsize=5)
def fibo_using_lru_cache(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fibo_using_lru_cache(n - 1) + fibo_using_lru_cache(n - 2)
    return result


def fibo_bottom_up(n):
    fibo_table = [0, 1]
    for i in range(2, n + 1):
        fibo_table.append(fibo_table[i - 1] + fibo_table[i - 2])
    return fibo_table[n]


def fibo_space_optimized(n):
    a, b = 1, 2
    for i in range(n):
        a, b = b, a + b
    return a


num = 1000
print(fibo_bottom_up(num))
# for i in range(1, num + 1):
#     print(i, ':', fibo_space_optimized(i))

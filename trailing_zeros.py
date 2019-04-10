# program to find out trailing zeros in factorial of number


def trailingZeros(n):
    count = 0
    if n < 0:
        return -1
    i = 5

    while n // i > 0:
        count += n // i
        i *= 5
    return count


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


num = 20
print(fact(num))
print(trailingZeros(num))

# program to find ugly numbers(numbers with only prime factors 2,3,5) upto n.


def reduce(num, x):
    while(num % x == 0):
        num = num / x
    return num


def ugly(n):
    count = 1
    for i in range(2, n):
        i = reduce(i, 2)
        i = reduce(i, 3)
        i = reduce(i, 5)

        if i == 1:
            count += 1

    print(count)


ugly(11)

# from collections import defaultdict
# from collections import Counter
# d = {}
# d[0] = 9
# d[1] = 12
# d['sd'] = 3

# [print(D, ':', d[D]) for D in d]

# for key, value in d.items():
#     print(key, ':', value)

# A = [3, 63, 2, 7, 3, 8, 6, 358, 53, 1, 1, 1, 1]
# count = Counter(A)

# print(count.most_common(2))
# for c in count.items():
#     if c.values() == 3:
#         print(c.keys())

# squares = {x: x * x for x in range(1, 11)}
# print(squares)
# n = {}
# s = 'svslkvnslkvnfc'
# for ss in s:
#     n.append
#     (ss)
# print(n)


# def birthdayCakeCandles(ar):
#     ar.sort()
#     if ar[0] == ar[1]:
#         return len(ar)
#     count = 1
#     for i in range(len(ar) - 1, 0, -1):
#         if ar[i] > ar[i - 1]:
#             continue
#         else:
#             count += 1
#     return count


# a = [2, 3, 4, 4]
# print(birthdayCakeCandles(a))
# from collections import defaultdict
# a = defaultdict(set)
# print(a)
# a[1] = '1'
# print(a)
# a[2].add('2')   # this creates set
# print(a)
# a[2].add('23')
# print(a)
# a[1].add('12')  # but this does not
# print(a)

# a = [1, 2, 3, 4, 5, 6, 7]
# a[2:4] = 'replaced1','replaced2'
# print(a)
# n = 4
# new_grid = [[0 for i in range(n - 2)] for j in range(n)]
# print(new_grid)
# for i in range(n):
#     for j in range(n-2):
#         new_grid[i][j] = 1
# print(new_grid)
# new_grid[0][0] = 'first'
# print(new_grid)
# new_grid[1][3] = 'element'
# print(new_grid)


def primeFactors(n):
    i = 2
    l = 2

    while(i * i <= n):
        while n % i == 0:
            l = i
            n //= i
        i += 1
    if n > l:
        l = n
    print(l)


n = 17
primeFactors(n)

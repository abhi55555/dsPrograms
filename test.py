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
import math


def primality(n):
    if n == 1:
        return 'Not prime'
    sq = int(math.sqrt(n)) + 1
    for i in range(2, sq):
        if (n % i) == 0:
            return 'Not prime'

    return 'Prime'


print(primality(3057601))

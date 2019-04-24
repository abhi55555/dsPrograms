# program to print k closest points to origin
points = [(1, 3), (-4, 5), (2.35, 0.9), (0, 0.1), (23, 32), (1, 1.1)]
table = {}
newarr = []
for p in points:
    dist = p[0]**2 + p[1]**2
    table[dist] = p
    newarr.append(dist)
newarr.sort()
for i in range(4):
    print(table[newarr[i]])

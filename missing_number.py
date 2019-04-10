hashtable = {}
for i in range(10):
    hashtable[i] = 0


def missingNumber(A):
    for a in A:
        hashtable[a] += 1

    print(hashtable)

    for h in hashtable:
        if hashtable[h] == 0:
            print('Missing number is', h)
            return
    print('No missing number')


A = [0, 5, 4, 3, 1, 7, 8, 9, 9, 2]

missingNumber(A)

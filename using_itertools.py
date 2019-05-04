from itertools import permutations, combinations


def useItertools(string):

    permList = permutations(string)
    combList = combinations(string, 2)

    for perm in list(permList):
        print(''.join(perm))

    print('------')
    for comb in list(combList):
        print(''.join(comb))


# Driver program
if __name__ == "__main__":
    string = 'ABC'
    useItertools(string)

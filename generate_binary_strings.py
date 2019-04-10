# generate binary strings of length n
def appendAtBeginning(x, l):
    return [x + element for element in l]


def bitString(n):
    if n == 0:
        return []
    if n == 1:
        return ['0', '1']
    else:
        return (appendAtBeginning('0', bitString(n - 1)) + (appendAtBeginning('1', bitString(n - 1))))


print(bitString(2))

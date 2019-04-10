# find two numbers in array whose sum is K


def twoSum(array, K):

    tempDict = {array[0]: 0}                   # here key is element of array and value is index of element
    for i in range(1, len(array)):
        checkNum = K - array[i]
        if(checkNum in tempDict.keys()):
            return [tempDict[checkNum], i]
        else:
            tempDict[array[i]] = i


A = [4, 2, 6, 8, 4, 2]

print(twoSum(A, 10))

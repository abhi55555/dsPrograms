# class to implement Binary Heap


class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        percolateUp(self.currentSize)

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[(i * 2) + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolateDown(self, i):
        while (i * 2) <= self.currentSize:
            minichild = self.minChild(i)
            if self.heapList[i] > self.heapList[minichild]:
                self.heapList[i], self.heapList[minichild] = self.heapList[minichild], self.heapList[i]
            i = minichild

    def deleteMin(self):
        retainval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percolateDown(1)
        return retainval

    def buildHeap(self, array):
        i = len(array) // 2
        self.currentSize = len(array)
        self.heapList = [0] + array[:]
        while i > 0:
            self.percolateDown(i)
            i -= 1


A = [9, 4, 3, 8, 2, 10, 23, 11, 5]

newheap = BinaryHeap()
newheap.buildHeap(A)
print(newheap.deleteMin())

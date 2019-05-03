import heapq


class StreamMedian:
    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        self.n = 0

    def insert(self, num):
        if self.n % 2 == 0:
            heapq.heappush(self.maxHeap, -1 * num)
            self.n += 1

            if len(self.minHeap) == 0:
                return

            if (-1 * self.maxHeap[0]) > self.minHeap[0]:
                toMin = -1 * heapq.heappop(self.maxHeap)
                toMax = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1 * toMax)
                heapq.heappush(self.minHeap, toMin)
        else:
            toMin = -1 * heapq.heappushpop(self.maxHeap, -1 * num)
            heapq.heappush(self.minHeap, toMin)
            self.n += 1

    def getMedian(self):
        if self.n % 2 == 0:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -1 * self.maxHeap[0]


arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [10, 11, 12, 13, 14]

s1 = StreamMedian()
for n in arr1:
    s1.insert(n)

print(s1.getMedian())

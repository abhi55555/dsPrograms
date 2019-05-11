# program to find maximun element in sliding window

from collections import deque


def maxSlidingWindow(A, k):
    deq = deque()

    for i in range(k):
        while deq and A[deq[-1]] <= A[i]:
            deq.pop()
        deq.append(i)

    for i in range(k, len(A)):
        print(str(A[deq[0]]) + ' ', end=' ')
        while deq and deq[0] <= i - k:           # sliding left part of window
            deq.popleft()
        while deq and A[deq[-1]] <= A[i]:        # if last element is smaller than current element pop it
            deq.pop()
        deq.append(i)

    print(str(A[deq[0]]))


A = [3, 5, 1, 7, 3, 5, 2, 8, 9]
k = 3
maxSlidingWindow(A, k)

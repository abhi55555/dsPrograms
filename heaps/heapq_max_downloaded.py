import heapq_max
arr = [4, 3, 33, 90, 321, 23, 567]

heapq_max.heapify_max(arr)
print(arr)
print(heapq_max.heappop_max(arr))
heapq_max.heappush_max(arr, 999)
print(arr)
heapq_max.heapreplace_max(arr, 100)
print(arr)

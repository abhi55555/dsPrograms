import heapq

list1 = [2, 6, 7, 2, 1, 9, 12, 11, 34]

heapq.heapify(list1)

print(list1)

heapq.heappush(list1, 4)

print(list1)

print('Element to be popped is ->', heapq.heappop(list1))

print(list1)

list2 = list1

print(heapq.heappushpop(list1, 1))           # first push then pop
print(heapq.heapreplace(list2, 1))			 # first pop then push
print(list1)
print(list2)

print(heapq.nlargest(4, list1))
print(heapq.nlargest(4, list1)[-1])          # prints 4th largest number in heap
print(heapq.nsmallest(3, list1))
print(heapq.nsmallest(3, list1)[-1])		 # prints 3rd smallest number in heap

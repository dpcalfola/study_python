import heapq

arr = [5, 89, 3, 1, 23, 7, 2]

for _ in range(len(arr)):
    print(heapq.heappop(arr))
    print(arr)

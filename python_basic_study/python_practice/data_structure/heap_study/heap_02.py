import heapq

arr = [i for i in range(10, 0, -1)]
print(arr)

for _ in range(len(arr)):
    print(heapq.heappop(arr))

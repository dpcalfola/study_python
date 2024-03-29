import heapq

arr = [5, 1, 3, 89, 23, 7, 2]
heap = []

for i in arr:
    heapq.heappush(heap, i)

print(heap)

for _ in range(len(heap)):
    print("heap : ", heapq.heappop(heap))


# 정렬되지 않은 배열을 heap pop 할 경우
# 처음엔 루트(index:0) 가 pop
# 이후 다음 최소값을 루트에 위치시킴
for _ in range(len(arr)):
    print("arr : ", heapq.heappop(arr))

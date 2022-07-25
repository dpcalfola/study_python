import heapq

arr = [5, 89, 3, 1, 23, 7, 2]

for _ in range(len(arr)):
    print(heapq.heappop(arr))
    print(arr)

# < 출력 >
# 5
# [2, 89, 3, 1, 23, 7]
# 2
# [3, 89, 7, 1, 23]
# 3
# [7, 89, 23, 1]
# 7
# [1, 89, 23]
# 1
# [23, 89]
# 23
# [89]
# 89
# []

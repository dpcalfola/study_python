from collections import deque

list_a = [1, 2, 3, 4]

que = deque(list_a)

print(que)
print(que.popleft())
print(que)

from collections import deque
import random

rand_list: list = random.sample(range(10), 10)
print(rand_list)

q = deque(rand_list)
print(q)

sorted_list: list = []

while len(q):
    sorted_list.append(q.pop())

print(sorted_list)

# Queue is just queue
# Do not confuse with heap(

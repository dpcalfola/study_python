import random

num_01 = random.randrange(0, 3)
print(num_01)

nums = list(range(0, 11))
print(nums)
print(*nums)

nums_01 = random.sample(nums, 3)
print(nums_01)

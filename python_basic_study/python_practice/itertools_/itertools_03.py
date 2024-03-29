import sys
from itertools import permutations, combinations

a1 = [1]
b1 = [2]
c1 = a1 + b1
print(c1)

# a, b, c, d = map(int, sys.stdin.readline().split())
a, b, c, d = 2, 1, 1, 1
arr = ["+"] * a + ["-"] * b + ["*"] * c + ["//"] * d
print(arr)

per_arr = list(permutations(arr))
print(per_arr)
print(len(per_arr))
per_set = set(per_arr)
print(len(per_set))

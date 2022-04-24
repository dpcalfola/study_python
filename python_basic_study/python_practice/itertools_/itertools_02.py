from itertools import combinations, permutations

a = list(combinations(range(1, 5), 2))

print(a)
print(len(a))

b = list(permutations(range(1, 5), 2))

print(b)
print(len(b))

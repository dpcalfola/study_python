from itertools import permutations

a = ["a", "b", "c"]

per_a = list(permutations(a, 2))
print(per_a)

for i in per_a:
    print(*i)

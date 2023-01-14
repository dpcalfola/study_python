s = "ABCDEFG"

# Explain: for i in range(A. B, C), concentrate on A, B, C.
# A: start -> start i at last index of s,
# B: stop -> stop i at 0,
# C: step -> step i by -1 (decrement)
for i in range(len(s) - 1, -1, -1):
    print(i, (s[i]))

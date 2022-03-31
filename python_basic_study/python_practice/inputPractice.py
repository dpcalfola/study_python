import sys

# input as one variable
a = sys.stdin.readline()
print(a)

# input as multiple variable (sting)
c, d = sys.stdin.readline().split()
print(c, d)

# input as list
# type must be stated
list_input = list(map(int, sys.stdin.readline().split()))
print(list_input)

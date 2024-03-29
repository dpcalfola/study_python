# license()

list1 = range(10, 40, 1)  # from 10 .<40 step by 1
print(list1)

for i in list1:
    print(i, end=",")

print()

for i in range(10, 2, -2):
    print(i, end=" ")

print()

str1 = "python"
print(str1)

str1 = """
python
java
javascript
swift
"""
print(str1)

str1 = "python"
print(str1[0])

list1 = []
for i in str1:
    list1.append(i)

print(list1)

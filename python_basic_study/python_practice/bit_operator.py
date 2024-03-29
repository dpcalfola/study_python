a = 3
b = 13

# 2 진수 출력
print("{0:b}".format(a).zfill(8))
print("{0:b}".format(b).zfill(8))
print("{0:b}".format(a ^ b).zfill(8))
print(a ^ b)

# xor
# -> 교집합의 여집합
# 같을 경우 0
# 다를 경우 1

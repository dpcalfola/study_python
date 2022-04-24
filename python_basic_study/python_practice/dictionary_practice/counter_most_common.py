import collections

a = [1, 3, 8, -2, 2, 8, 2, 8]
dic_a = collections.Counter(a)
print(dic_a)

# 빈도수가 높은 순서로 tuple list로 반환
print(dic_a.most_common())

# 빈도수가 높은 2개를 tuple list로 반환
tuple_list_a = dic_a.most_common(2)
print(tuple_list_a)

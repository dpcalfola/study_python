import collections

# 빈도수가 같을 떄 어떤 숫자가 우선으로 나오는지 테스트

a = [2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9, 10, 11]
counter_dic_a = collections.Counter(a)
print(counter_dic_a)

b = [9, 9, 9, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 10, 11]
counter_dic_b = collections.Counter(b)
print(counter_dic_b)

# 결론
# 앞에 있는게 먼저 나온다.

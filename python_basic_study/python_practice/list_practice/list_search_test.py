a = [1, 2, 3, 4, 5]

print(a.index(5))  # 4
# print(a.index(9))  # ValueError
search_num = 9
try:
    print(a.index(search_num))
except ValueError:
    print(f'{search_num} not in list')

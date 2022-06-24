import random

dic_a = {}

rand_key_list = []

for i in range(10):
    random_num = random.randrange(0, 100)
    rand_key_list.append(random_num)

for i in rand_key_list:
    random_num = random.randrange(0, 100)
    dic_a[i] = random_num

print(dic_a)
print()

# print all element
for k, v in dic_a.items():
    print(f'{k}: {v}')

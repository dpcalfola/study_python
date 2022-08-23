is_a: bool = True
is_b: bool = True

print(is_a + is_b)

print(True + False)
print(False)
print(False + 1)
print(True + 1)

bool_list_a: list = [True]
bool_list_b: list = [False]
bool_list_c: list = bool_list_a + bool_list_b

print(bool_list_c)
if bool_list_c[0]:
    print('bool_list_c[0] is True')

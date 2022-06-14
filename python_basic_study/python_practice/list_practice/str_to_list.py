str_a: str = 'abcde'

list_a_0 = [i for i in str_a]
print('list_a : ', list_a_0)

list_a_2: list = list(map(str, str_a))
print('list_a_2 : ', list_a_2)

list_a_3: list = list(str_a)
print('list_a_3 : ', list_a_3)

int_b = 12345
# list_b_0: list = list(int_b)
# -> It doesn't working. Maybe argument of list() should be string
list_b_0: list = list(str(int_b))
print('list_b_0: ', list_b_0)
print('type(list_b_0[0]) : ', type(list_b_0[0]))

list_b_1: list = list(map(int, str(int_b)))
print('list_b_1 : ', list_b_1)
print('type(list_b_1[0]) : ', type(list_b_1[0]))


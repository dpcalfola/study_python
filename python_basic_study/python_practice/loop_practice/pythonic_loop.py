# pythonic loop

arr_1 = [0 for _ in range(5)]
print(arr_1)

arr_2 = [i for i in range(5)]
print(arr_2)

arr_3 = [[i for i in range(5)] for _ in range(5)]
print(arr_3)

arr_4 = [[i + j for i in range(5)] for j in range(0, 25, 5)]
print(arr_4)

size = 3
arr_5 = [[i + j for i in range(size)] for j in range(0, size ** 2, size)]
print(arr_5)

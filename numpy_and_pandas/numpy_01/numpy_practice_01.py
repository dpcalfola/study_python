import numpy as np

data_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_2 = [[1, 2, 3.0], [4, 5, 6], [7, 8, 9]]
np_a = np.array(data_1)
np_b = np.array(data_2)

print(np_a)
print(np_b)
print()

# numpy .dtype 자료형을 알아본다
# 추천하지 않는 방법 ( element 자료형을 알아 볼 수 없음 )
print(type(np_a))
print(type(np_b))
# 추천방법 (numpy 내장 함수 사용)
print(np_a.dtype)
print(np_b.dtype)

print()

# print(dir(np_a))

# type casting
np_a = np_a.astype(np.float64)
np_b = np_b.astype(np.int64)
print('np_a : \n' + str(np_a) + '\n')
print('np_b : \n' + str(np_b) + '\n')

# get element
print(np_a[0][1])
print(np_a[0])



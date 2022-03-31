import numpy as np

print('---- 1차원 행렬 ----r')
array_01 = np.arange(1, 10, 2)
print(array_01)
print(array_01[2])
print()

# 1차원 행렬
print('---- 2차원 행렬 ----')
# element 요소의 개수 (1~9 == 9개 ) 와 (3 by 3 ) 의 개수가 맞지 않으면 에러
array_02 = np.arange(1, 10).reshape(3, 3)
print(array_02)
print()

# 3차원 행렬
print('---- 3차원 행렬 ----')
# 큰 괄호 안에 3개 -> 2개 - > 2개 순으로 구성
array_03 = np.arange(1, 13).reshape(3, 2, 2)
print(array_03)
print()

# 결측치 ? == nan
# 결측치는 정수형에서 사용 할 수 없다
print('---- nan ----')
print(np.nan)

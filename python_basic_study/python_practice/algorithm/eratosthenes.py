import math


# 배열의 결과가 True -> 소수
# 배열의 index -> 숫자
def prime_arr(max_int: int) -> list:
    # boolean 배열 생성
    arr = [True] * (max_int + 1)
    limit = math.floor(math.sqrt(max_int))

    # 0 과 1 은 소수가 아님으로 마킹
    arr[0] = False
    arr[1] = False

    for i in range(2, limit):
        # i가 소수일 경우
        if arr[i]:
            # 소수의 제곱부터 최대범위까지 i의 배수만큼 걸어가며 False 로 마킹
            for j in range((i**2), len(arr), i):
                arr[j] = False
    return arr


arr_100 = prime_arr(100)
cnt = 0
for i in arr_100:
    print(cnt, i)
    cnt += 1

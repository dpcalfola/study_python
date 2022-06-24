import sys

# input_string = sys.stdin.readline()
input_string = "OneTwoThreeFourFiveSixSevenEightNineTen123"
# 열개씩 끊어 출력하기

# .removesuffix()
# suffix : 접미사
# 문자열 매개변수가 접미사로 존재할 경우 접미사를 잘라내고 앞을 남긴다
# 접미사로 존재하지 않을 경우 아무것도 잘라내지 않는다

s = input_string.removesuffix("Ten")  # 아무것도 잘리지 않음
print(s)

s = input_string.removesuffix("eTen123")  # 접미사를 자르고 나머지를 반환
print(s)

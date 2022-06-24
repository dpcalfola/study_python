string_a = "012345678"

result = string_a[1:8:2]  # index 1 이상 8 미만까지 2칸식 증가 # 1357
result_2 = string_a[2:]  # index 2 이상 끝까지 # 2345678
result_3 = string_a[:3]  # index 3 미만까지 # 012
result_4 = string_a[:-3]  # 뒤에서부터 3개 제거하고 전부 # 012345
result_5 = string_a[-3:]  # (뒤에서부터 3개) 부터 끝까지 # 678
result_6 = string_a[4]  # index 4 # 4
result_7 = string_a[-1]  # 마지막 글자

print(result)  # 1357
print(result_2)  # 2345678
print(result_3)  # 012
print(result_4)  # 012345
print(result_5)  # 678
print(result_6)  # 4
print(result_7)  # 8


# null string 일 경우 substring 문법 시도할 경우 에러 발생
string_b = ''
result_b_1 = string_b[0]
print(result_b_1)

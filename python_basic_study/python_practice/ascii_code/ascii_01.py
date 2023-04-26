# 1 ~ 26 -> A, B ... Z
# cha(65) ==> A


n_1 = 1
n_2 = 26
n_3 = 52  # AZ

c_1 = chr(64 + n_1)
c_2 = chr(64 + n_2)

print(c_1)
print(c_2)

print(25 // 26)
print("-----------")


def get_char(n: int) -> chr:
    s = ""

    while n != 0:
        reminder = n % 26
        n //= 26

        if reminder == 0:
            s += "Z"
            n -= 1
        else:
            s += chr(64 + reminder)
        # print('reminder', reminder)

    return s


print(get_char(1), 1)
print(get_char(26), 1)
print(get_char(27), 27)
print(get_char(53), 53)
print(get_char(52), 52)

print("-----")
print(get_char(26))

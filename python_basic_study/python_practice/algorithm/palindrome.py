str_01 = "asdf1fdsa"
str_02 = "asdf1fdsa2"


def is_palindrome(s: str) -> bool:
    s_list = list(s)
    while len(s_list) > 1:
        if s_list.pop(0) != s_list.pop():
            return False

    return True


print(is_palindrome(str_01))
print(is_palindrome(str_02))

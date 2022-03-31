string1 = "3"

# String.find : return index of character , if it can't find, return -1
print(string1.find("t"))

# String.find : return index of character , if it can't find, ValueError : substring not found
# both of .find, .index distinguish uppercase and lowercase
# index_of_string = string1.index('n')
# print(index_of_string)

print(string1.isalpha())  # only has alphabet return True
print(string1.isalnum())  # 알파벳 혹은 숫자로 이루어져 있을 경우 True

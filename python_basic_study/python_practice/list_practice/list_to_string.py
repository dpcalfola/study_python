import re

list_a = [1, 3, 4, 5, 6, 7]

print(*list_a)

string_a = str(list_a)

removed_string = re.sub("[\\[\\],]", "", string_a)

print(removed_string)

print(re.sub("[\\[\\],]", "", string_a))

dict_a: dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

print(f'dict_a.pop("c", None): {dict_a.pop("c", None)}')
print(dict_a)

dict_a.pop("a")

# Error: There's no key: "e" Raised KeyError
# dict_a.pop("e")

# .pop(key, None) => If there no key to pop,
# Instead of raising Error, return None
dict_a.pop("e", None)
print(dict_a)

print(f'dict_a.pop("e", None): {dict_a.pop("e", None)}')

print(type(dict_a.pop("e", None)))

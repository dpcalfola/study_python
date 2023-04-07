class Person:
    def __init__(self, name: str):
        self.name = name


person_1 = Person("Fola")

# getattr => Get the value of attribute
name_1 = getattr(person_1, "name")
print(name_1)

# setattr => Update the value of attribute
setattr(person_1, "name", "Stephen")
print(person_1.name)

# hasattr => Return bool whether attribute exist on an object or not
if hasattr(person_1, "name"):
    print(f'object has "name" attribute')
else:
    print(f'object has not "name" attribute')

if hasattr(person_1, "age"):
    print('object has "age" attribute')
else:
    print('object has not "age" attribute')

class Person:
    def __init__(self, name, age, address, is_handsome):
        self.name = name
        self.age = age
        self.address = address
        self.is_handsome = is_handsome


me = Person('fola', '36', 'Kyenggido', False)

if me:
    print(me.age)

str_a = 'abced'

if str_a:
    print(str_a)

if me.is_handsome:
    print('handsome')
else:
    print('not handsome')

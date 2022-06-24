a: str = '12345'

is_digit_a = a.isdigit()

print(is_digit_a)

a_int: int = int(a)
print(a_int)

b: str = '-12345'
is_digit_b = b.isdigit()
print('is_digit_b:', is_digit_b)

is_numeric_b = b.isnumeric()
print(is_numeric_b)

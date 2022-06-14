def get_gcd(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b


print(get_gcd(10, 2))

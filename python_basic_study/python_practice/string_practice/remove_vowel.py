def remove_vowel(w: str):
    word: str = w
    vowels = ['a', 'e', 'i', 'o', 'u']

    for c in word:
        if c.lower() in vowels:
            word = word.replace(c, "")

    return word


print(remove_vowel('abcdefg'))


def remove_vowel_and_next_char(w: str):
    word: str = w
    vowels = ['a', 'e', 'i', 'o', 'u']

    for c in word:
        if c.lower() in vowels:
            word = word.replace(c, "")

    return word
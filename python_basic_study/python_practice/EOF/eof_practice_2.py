last_input: str = '\n'


# eof
def non_eof():
    if last_input:
        print('something exist')
        return
    print('succeed eof')


def eof():
    if last_input.rstrip('\n'):
        print('something exist')
        return
    print('succeed eof')


non_eof()
eof()
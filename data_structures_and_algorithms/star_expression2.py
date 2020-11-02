def drop_first_last_letters(letters):
    _, *middle, _ = letters
    return ''.join(middle)

print(drop_first_last_letters('Leonardo'))



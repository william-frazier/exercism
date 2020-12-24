def is_valid(isbn):
    if isbn.find("X") != - 1:
        if isbn.find("X") != len(isbn) - 1:
            return False
    length = 0
    count = 10
    final = 0
    for number in isbn:
        if number in "0123456789X":
            try:
                final += count * int(number)
            except:
                final += count * 10
            length += 1
            count -= 1
    return (not final % 11) and (length == 10)

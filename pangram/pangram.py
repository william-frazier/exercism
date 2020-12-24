def is_pangram(sentence):
    letters = [0] * 26
    for character in sentence.upper():
        slot = ord(character) - 65
        if slot >= 0 and slot <= 25:
            if letters[slot] == 0:
                letters[slot] = 1
    return sum(letters) == 26
    

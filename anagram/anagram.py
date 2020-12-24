def find_anagrams(word, candidates):
    letter_dict = dict()
    result = []
    for letter in word:
        letter = letter.lower()
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    for poss in candidates:
        poss_letter_dict = dict()
        for letter in poss:
            letter = letter.lower()
            if letter not in poss_letter_dict:
                poss_letter_dict[letter] = 1
            else:
                poss_letter_dict[letter] += 1
        if poss_letter_dict == letter_dict:
            result.append(poss)
    return result
                

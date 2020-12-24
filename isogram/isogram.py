def is_isogram(string):
    char_list = [i for i in string.lower() if i.isalpha()]
    return len(char_list) == len(set(char_list))


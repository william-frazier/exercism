import re
from collections import defaultdict

def count_words(sentence):
    sentence = re.sub(r'[^A-Za-z0-9\' ]+', ' ', sentence)
    word_list = sentence.lower().split()
    final_dict = defaultdict(int)
    for word in word_list:
        word = word.strip("'")
        final_dict[word] += 1
    return final_dict

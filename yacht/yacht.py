

import collections

# Score categories.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 9


def score(dice, category):
    count = collections.Counter(dice).most_common(1)[0]
    if category <= 6:
        return dice.count(category) * category
    elif category == 7:
        if len(set(dice)) == 2 and count[1] == 3:
            return sum(dice)
    elif category == 8:
        if count[1] >= 4:
            return count[0] * 4
    elif category == 9:
        return sum(dice)
    elif category == 10:
        if max(dice) == 5 and count[1] == 1 and min(dice) == 1:
            return 30
    elif category == 11:
        if max(dice) == 6 and count[1] == 1 and min(dice) == 2:
            return 30
    elif category == 50:
        if count[1] == 5:
            return 50
    return 0
    

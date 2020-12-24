def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_list = sorted(scores, reverse=True)
    return sorted_list[:3]
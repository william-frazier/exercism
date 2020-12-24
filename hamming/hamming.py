def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("The two strings must be of the same length.")
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            count += 1
    return count

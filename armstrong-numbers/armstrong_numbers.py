def is_armstrong_number(number):
    total = 0
    for i in range(len(str(number))):
        # this line looks messy
        # the first part is just an easy way of finding a given digit
        # if we're handling huge numbers then it probably becomes more
        # efficient to cast to a string and then select individual chars
        # and cast them back to ints
        total += (number // 10**i % 10)**(len(str(number)))
    return total == number
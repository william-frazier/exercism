def convert(number):
    ret_string = ''
    if not(number % 3):
        ret_string += "Pling"
    if not(number % 5):
        ret_string += "Plang"
    if not(number % 7):
        ret_string += "Plong"
    return ret_string if ret_string else str(number)
   
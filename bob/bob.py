def response(hey_bob):
    hey_bob = hey_bob.replace(" ","")
    hey_bob = hey_bob.replace("\t","")
    hey_bob = hey_bob.replace("\r","")
    hey_bob = hey_bob.replace("\n","")
    if hey_bob == '':
        return "Fine. Be that way!"
    if hey_bob.upper() == hey_bob and hey_bob.lower() != hey_bob:
        if hey_bob[-1] == '?':
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if hey_bob[-1] == "?":
        return "Sure."
    return "Whatever."

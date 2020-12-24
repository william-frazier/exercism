def recite(start_verse, end_verse):
    switcher = {
            1: ["first", "a Partridge in a Pear Tree."],
            2: ["second", "two Turtle Doves, "],
            3: ["third", "three French Hens, "],
            4: ["fourth", "four Calling Birds, "],
            5: ["fifth", "five Gold Rings, "],
            6: ["sixth", "six Geese-a-Laying, "],
            7: ["seventh", "seven Swans-a-Swimming, "],
            8: ["eighth", "eight Maids-a-Milking, "],
            9: ["ninth", "nine Ladies Dancing, "],
            10: ["tenth", "ten Lords-a-Leaping, "],
            11: ["eleventh", "eleven Pipers Piping, "],
            12: ["twelfth", "twelve Drummers Drumming, "]
            }
    if start_verse != 1:
        switcher[1][1] = "and " + switcher[1][1] 
    day = switcher.get(start_verse)[0]
    opening = "On the {day} day of Christmas my true love gave to me: "
    current = start_verse
    while current >= 1:
        opening += switcher.get(current)[1]
        current -= 1
    opening = [opening.format(day=day)]
    if start_verse != end_verse:
        opening += recite(start_verse + 1, end_verse)
    return opening

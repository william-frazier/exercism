# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = ["_"] * len(word)

    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError("You've already lost!")
        elif self.get_status() == STATUS_WIN:
            raise ValueError("You've already won!")
        if char not in self.word or char in self.masked_word:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
            return
        current_word = self.word
        location = current_word.find(char)
        i = 0
        while location != -1:
            i += 1
            self.masked_word[location] = char
            location = current_word.find(char,i)
        return

    def get_masked_word(self):
        masked_word_str = ""
        for i in self.masked_word:
            masked_word_str += i
        return masked_word_str

    def get_status(self):
        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        return self.status

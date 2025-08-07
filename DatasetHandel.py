import random

class DatasetHandel:
    def __init__(self, filepath="words.txt"):
        with open(filepath, 'r') as file:
            self.words = [line.strip() for line in file if line.strip()]

    def random_word_from_set(self):
        return random.choice(self.words)

    def validate_word(self, guessed_word):
        return guessed_word in self.words
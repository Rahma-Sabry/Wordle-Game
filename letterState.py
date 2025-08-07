class LetterState:
    def __init__(self, letter):
        self.letter = letter
        self.is_in_secret_word = False
        self.is_correct_position = False
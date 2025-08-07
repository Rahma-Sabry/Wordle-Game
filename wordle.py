class Wordle:
    MAX_AteMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret_word: str):
        self.secret_word: str = secret_word
        self.attempts = []

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret_word

    @property
    def remaining_attempts(self):
        return self.MAX_AteMPTS - len(self.attempts)

    def add_attempt(self, attempt: str):
        if len(attempt) != self.WORD_LENGTH:
            raise ValueError(f"Attempt must be {self.WORD_LENGTH} characters long.")
        if not self.can_attempt:
            raise ValueError("No more attempts allowed.")
        if attempt in self.attempts:
            raise ValueError("Attempt already made.")
        self.attempts.append(attempt)

    @property
    def can_attempt(self):
        return len(self.attempts) < self.MAX_AteMPTS and not self.is_solved
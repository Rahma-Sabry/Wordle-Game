from wordle import Wordle
from DatasetHandel import DatasetHandel
def main():
    # Your main code here
    print("Starting Wordle game...")
    dataset = DatasetHandel("words.txt")
    secret_word = dataset.random_word_from_set()
    game = Wordle(secret_word)
    while not game.is_solved and game.can_attempt:
        attempt = input(f"Enter your {game.WORD_LENGTH}-letter guess (attempts left: {game.remaining_attempts}): ") 
        if dataset.validate_word(attempt):
            try:
                game.add_attempt(attempt)
                print(f"Attempt '{attempt}' added. Remaining attempts: {game.remaining_attempts}")
                letter_states = game.get_letter_states(attempt)
                for letter_state in letter_states:
                    print(f"Letter: {letter_state.letter}, In word: {letter_state.is_in_secret_word}, Correct position: {letter_state.is_correct_position}")
            except ValueError as e:
                print(e)    
        else:
            print(f"'{attempt}' is not a valid word. Please try again.")   
    if game.is_solved:
        print(f"Congratulations! You've solved the word: {game.secret_word}")
    else:
        print(f"Game over! The secret word was: {game.secret_word}")
    #print(f"Secret word is: {game.secret_word}")
    #game.play()

if __name__ == "__main__":
    main()
# Wordle Game (Python Console Version)

A simple console-based Wordle game implemented in Python.

## Features

- Play the classic Wordle game in your terminal.
- Colored feedback for each letter (green, yellow, gray) using `colorama`.
- Validates guesses against a word list.
- Tracks attempts and notifies when the game is won or lost.

## How to Run

1. **Install dependencies**  
   Make sure you have Python 3 installed.  
   Install `colorama` if you don't have it:
   ```
   pip install colorama
   ```

2. **Prepare your word list**  
   Place a `words.txt` file in the project directory, with one valid word per line.

3. **Run the game**
   ```
   python playWordle.py
   ```

## File Structure

- `playWordle.py` — Main game loop and user interface.
- `wordle.py` — Game logic.
- `DatasetHandel.py` — Handles loading and validating words.
- `letterState.py` — Represents the state of each letter in a guess.
- `words.txt` — List of valid words (one per line).

## Example Gameplay

```
Starting Wordle game...
Enter your 5-letter guess (attempts left: 6): house
[Colored output for each letter]
...
Congratulations! You've solved the word: HOUSE
```

## License

MIT
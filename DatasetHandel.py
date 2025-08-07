import random
with open("words.txt", 'r') as file:
        words = [line.strip() for line in file if line.strip()]
def randomWordFromSEt():  
    return random.choice(words)
def validateWord(gussedWord):
    if gussedWord in words:
        return True
    else:
        return False
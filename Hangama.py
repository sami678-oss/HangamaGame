import random

def select_random_word():
    words = ['python', 'hangman', 'programming', 'developer', 'challenge', 'random', 'game', 'computer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = select_random_word()
    guessed_letters = set()
    attempts_remaining = 6
    
    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    
    while attempts_remaining > 0:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts_remaining}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! {guess} is in the word.")
        else:
            attempts_remaining -= 1
            print(f"Sorry, {guess} is not in the word.")
        
        if set(word) <= guessed_letters:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nYou've run out of attempts. The word was:", word)

hangman()
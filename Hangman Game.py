import random

def hangman():
    # List of words to choose from
    word_list = ["python", "hangman", "programming", "developer", "language", "function", "variable"]
    word = random.choice(word_list)  # Randomly select a word
    guessed_word = ["_"] * len(word)  # Placeholder for the guessed word
    attempts = 7  # Set the maximum number of incorrect guesses
    guessed_letters = set()  # Track guessed letters

    print("Welcome to Hangman!")
    print("You have", attempts, "attempts to guess the word.")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            # Update the guessed word
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts -= 1
            print("Incorrect. You have", attempts, "attempts remaining.")

        print(" ".join(guessed_word))

    # End game message
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

# Run the game
hangman()

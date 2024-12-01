# niha2708-CodeAlpha_Hangman_Game

Hangman Game 🎮:
A fun and interactive text-based Hangman game implemented in Python! This game brings the classic word-guessing challenge to your command-line interface. The player attempts to guess a randomly chosen word by entering one letter at a time, aiming to uncover the hidden word before running out of chances. It’s a simple yet engaging game, perfect for both beginners learning to code and those who love classic games.

✨ Features:
Random Word Selection: The game picks a word randomly from a predefined list, ensuring variety with every play.
Real-time Feedback:
Displays the current state of the word (with underscores for hidden letters).
Updates the display after each guess, showing correctly guessed letters in their respective positions.
Limited Guesses: Players have a set number of incorrect guesses, encouraging strategic letter selection.
Progress Tracking: The number of attempts remaining and previously guessed letters are displayed after every guess.
Win/Loss Outcomes:
Players win if they uncover the entire word.
The game ends with a loss when the incorrect guess limit is reached.

🛠️ How It Works
Start the Game: When the program is launched, it selects a random word and initializes the game environment.
Guessing Process: The player inputs a single letter per turn:
If the letter is correct, it fills in the appropriate positions in the word.
If the letter is incorrect, it counts as a wrong guess, reducing the remaining attempts.
Game End:
Win: The player successfully guesses all letters of the word.
Lose: The player uses up all allowed incorrect guesses.
In either case, the full word is revealed at the end.

📂 Folder Structure
Hangman/
├── main.py          # Core game logic
├── words.txt        # Word list for random selection
└── README.md        # Documentation

🚀 Getting Started
Prerequisites
Python 3.x installed on your system.

Installation
git clone https://github.com/your-username/hangman-game.git
cd hangman-game
Run the game:
python main.py

🎉 Customization
Word List: Edit the words.txt file to add or customize the set of words used in the game.
Guess Limit: Adjust the MAX_ATTEMPTS variable in main.py to change the number of incorrect guesses allowed.

🧑‍💻 Contribution
Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or new features.

Feel free to tweak this based on your project’s specifics or style preferences!
Thank You so much!....



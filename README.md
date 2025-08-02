# -CodeAlpha_HangmanGame
Hangman game( in python ) project for  Code Alpha Internship  Task 1  
 CodeAlpha Task 1: Hangman Game 
This is a simple text-based Hangman game written in Python for the CodeAlpha internship.
THE FEATURES  IN THE PROJECT:
5 predefined words
6 incorrect guess limit
Tracks guessed letters
Console-based interaction
explanation of the code by step by step :
-import random
We use this to randomly pick a word from the list.
random.choice() selects one item randomly.
words = ["python", "apple", "banana", "orange", "laptop"]
These are the 5 predefined words from which the game picks one.
secret_word = random.choice(words)
Randomly selects one word from the list to be guessed by the player
4. Initialize Game Variables
guessed_word = ["_"] * len(secret_word)
attempts = 6
guessed_letters = []
guessed_word shows underscores for unguessed letters (e.g., ["_", "_", "_"])
attempts is set to 6 (maximum wrong guesses).
guessed_letters stores all guessed letters to prevent repetition.
 5. Display Welcome Message
 print("🎮 Welcome to Hangman Game!")
print("Guess the word by entering one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")
Greets the user and explains the rules briefly.
6. Main Game Loop
while attempts > 0 and "_" in guessed_word:
The game continues until the player either:
Wins (no _ left, i.e., guessed the word), or
Loses (attempts reach 0)
7. Inside the Game Loop
    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()
Displays the current guessed state of the word and previously guessed letters.
 8. Input Validation
     if not guess.isalpha() or len(guess) != 1:
        print(" Invalid input. Please enter a single alphabet letter.\n")
        continue
        Checks if the input is a single letter.

If not, it gives a warning and skips the rest of the loop.
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue
        9. Check for Repeated Guesses
            if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue
Avoids penalizing the player for guessing the same letter again.
Update Guessed Letters List
    guessed_letters.append(guess)
Adds the valid guessed letter to the list.
11. Check If Guess is Correct
    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
If the guessed letter is in the word:
Updates guessed_word with the correct positions
Wrong Guess Handling
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.\n")
If the guess is wrong, reduce attempts by 1 and show remaining tries.
13. End of Game
if "_" not in guessed_word:
    print(f" Congratulations! You guessed the word: {secret_word}")
else:
    print(f" Game Over! The word was: {secret_word}")
After exiting the loop:
If all letters are guessed, player wins.
Else, they lose and the word is revealed.
Takes new input and converts it to lowercase.
In above project we can guess  only in the given word
it having limited guess chance 
Concepts Used are in this project 
random module
while loop and if-else logic
String and list manipulation
User input validation
TO RUN :
python hangman.py
What I Learned:
Loops and conditions
String and list manipulation
User input handling
for clear explanation you can refer my linked in:
https://www.linkedin.com/posts/avanthika-reddy-59924a32a_python-codealpha-internshipproject-activity-7357420263593922561-Tk0j?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFL5QsUBq7iWKE4pM6Q-10JjJXpqlo0jb6Y

import random
words = ["python", "apple", "banana", "orange", "laptop"]
word = random.choice(words)
guessed = "_" * len(word)
attempts = 6
used_letters = []

while attempts > 0 and "_" in guessed:
    print(f"\nWord: {guessed}")
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter.")
        continue
    used_letters.append(guess)

    if guess in word:
        guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if "_" not in guessed:
    print(f"Congrats! You guessed the word: {word}")
else:
    print(f"Game over. The word was: {word}")

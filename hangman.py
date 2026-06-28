import random

# -----------------------------
# Hangman Game - CodeAlpha Task
# -----------------------------

# List of predefined words
words = ["apple", "python", "orange", "coffee", "coding"]

# Randomly select a word
secret_word = random.choice(words)

# Create hidden display
display = ["_"] * len(secret_word)

# Number of lives
lives = 6

# Store guessed letters
guessed_letters = []

print("=" * 40)
print("      WELCOME TO HANGMAN GAME")
print("=" * 40)
print("Guess the word one letter at a time.")
print(f"You have {lives} lives.\n")

# Game Loop
while lives > 0:

    # Display current progress
    print("\nCurrent Word:")
    print(" ".join(display))

    print("\nGuessed Letters:", " ".join(guessed_letters))

    # User input
    guess = input("\nEnter a letter: ").lower()

    # Input Validation
    if len(guess) != 1:
        print("❌ Please enter ONLY one letter.")
        continue

    if not guess.isalpha():
        print("❌ Please enter alphabet letters only.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:

        print("✅ Correct Guess!")

        # Reveal matching letters
        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                display[position] = guess

    else:
        lives -= 1
        print("❌ Wrong Guess!")
        print(f"Lives Remaining: {lives}")

    # Check Win
    if "_" not in display:
        print("\n🎉 CONGRATULATIONS!")
        print("You guessed the word:", secret_word.upper())
        break

# Check Lose
if lives == 0:
    print("\n💀 GAME OVER!")
    print("The correct word was:", secret_word.upper())

print("\nThanks for playing!")
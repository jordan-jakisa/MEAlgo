import random

word_list = ["python", "hangman", "programming", "developer", "terminal"]

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

display = ['_'] * word_lenght

attempts = 6
guessed_letters = []

while attempts > 0:
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in chosen_word:
        for i in range(word_lenght):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

    if "_" not in display:
        print("Congratulations, you've guessed the word!")
        break

if "_" in display:
    print(f"Sorry, you've run out of attempts. The word was: {chosen_word}")
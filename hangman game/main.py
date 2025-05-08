import random

def hang():
    print("Welcome to the Hangman game!\nGuess the word one letter at a time.")

    words = ["iphone", "macbook", "laptop", "screen", "charger", "lights"]
    electronics = random.choice(words)
    guessed = ["-"] * len(electronics)
    guessed_letters = set()
    lives = 6

    while lives > 0 and "-" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Lives remaining:", lives)
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in electronics:
            for i, letter in enumerate(electronics):
                if letter == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            lives -= 1
            print("Wrong guess!")

    if "-" not in guessed:
        print("\nCongratulations! You guessed the word:", electronics)
    else:
        print("\nGame over! The word was:", electronics)

hang()


import random
from colorama import init, Fore

def main():
    init(autoreset=True)
    
    print(Fore.RESET + "Welcome to " + Fore.RED + "Hangman" + Fore.RESET + "!")
    print("Guess the word letter by letter before running out of attempts.")
    print(Fore.YELLOW + "Good luck!\n")

    words = ["hangman", "random", "intern", "codealpha", "clothing",
             "computer", "python", "program", "glasses", "programming",
             "science", "internship", "friends", "coding", "biology",
             "algebra", "university", "guesses", "attempts"
             ]  # Removed duplicate "science"

    play_again = True

    while play_again:
        chosen_word = random.choice(words).lower()
        guessed_letters = set()
        display_word = ["-"] * len(chosen_word)
        attempts = 10

        while attempts > 0 and "-" in display_word:
            print(Fore.RED + f"\nAttempts Remaining: {attempts}")
            print(Fore.BLUE + "Word: " + "".join(display_word))
            print(Fore.CYAN + f"Guessed Letters: {', '.join(sorted(guessed_letters))}")

            print(Fore.WHITE + "Type in a letter: ", end="")
            guess = input().lower()

            if not guess.isalpha() or len(guess) != 1:
                print(Fore.YELLOW + "Invalid input. Enter a single letter.")
                continue
            if guess in guessed_letters:
                print(Fore.YELLOW + "You already guessed that letter.")
                continue

            guessed_letters.add(guess)

            if guess in chosen_word:
                for index, letter in enumerate(chosen_word):
                    if letter == guess:
                        display_word[index] = guess
            else:
                attempts -= 1
                if attempts == 1:
                    print(Fore.RED + "Careful! Only one attempt left!")

        if "-" not in display_word:
            print(Fore.GREEN + f"\nCongratulations! You guessed the word: {chosen_word}")
        else:
            print(Fore.RED + f"\nYou lose! The word was: {chosen_word}")

        response = input("Play again? (yes/no): ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
